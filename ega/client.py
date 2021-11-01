"""
Client for interacting with EGA REST API.
"""
import logging
from json import JSONDecodeError
from pathlib import Path
from urllib.parse import quote_plus

import requests
from lxml import etree

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from graflipy import get_config
from graflipy.ega.metadata import submission, submissionset
from graflipy.ega.schema_1_5_0 import SUBMISSIONXSD, AddSchema, SubmissionType
from graflipy.exceptions import NotifiableError


EGACONF = get_config().ega
ERR_ACTION = 'Unhandled action %s'
ERR_AUTH = 'No token received; endpoint %s will be unavailable'
ERR_CRED_SRC = 'Exactly one of password or password_file is required'
ERR_FAILED = 'Submission failed. See output for details'
ERR_RESPONSE = 'Unexpected response %s: %s'
LOGGER = logging.getLogger(__name__)
MSG_SUCCEEDED = 'Submission succeeded'
SCHEMA_ARCHIVE = {
    AddSchema.ANALYSIS: 'analyses',
    AddSchema.STUDY: 'studies',
    AddSchema.POLICY: 'policies',
}
XMLCONF = SerializerConfig(pretty_print=True,
                           no_namespace_schema_location=SUBMISSIONXSD)


# alias for convenience
Action = SubmissionType.Actions.Action
Add = SubmissionType.Actions.Action.Add
Validate = SubmissionType.Actions.Action.Validate
Protect = SubmissionType.Actions.Action.Protect


class SubmissionFailed(NotifiableError):
    """
    Raise on failed submission
    """


class RequestFailed(Exception):
    """
    Raise on failed API request
    """


class FileUpload:
    """
    Associate a schema name with a data stream and provide some conveniently
    named attributes
    """
    def __init__(self, schema, stream):
        """
        Args:
            schema: AddSchema
            stream: io.TextIOBase, e.g. an open text file handle
        """
        self.schema = schema
        self.stream = stream
        self.data = stream.read()

    @property
    def filename(self):
        """
        From the stream name
        """
        return self.stream.name

    @property
    def formname(self):
        """
        From the schema name
        """
        return self.schema.value.upper()

    @property
    def source(self):
        """
        Alias for filename
        """
        return self.filename


class RESTClient:
    """
    Client for interacting with EGA REST API
    """

    def __init__(self, user, password=None, password_file=None, test=False,
                 timeout=120):
        """
        Exactly one of password or password_file is required

        Args:
            user: str username
            password: Optional[str] password
            password_file: Optional[str] location of a file containing the
                user's password
            test: bool if True then use API test endpoint otherwise production
            timeout: int use this timeout in requests
        """
        if (password is None) == (password_file is None):
            raise ValueError(ERR_CRED_SRC)
        password = (password or
                    Path(password_file).expanduser().read_text().strip())
        self.auth = (user, password)
        self.endpoint = (EGACONF.restUrlTest if test
                         else EGACONF.restUrlProduction)
        self.endpoint_new = None if test else EGACONF.restUrlNew
        self.timeout = timeout
        self.serializer = XmlSerializer(config=XMLCONF)
        self.login_token = None
        # get login token for new API
        try:
            response = requests.post(
                self.endpoint_new + 'login',
                data={'username': user,
                      'password': quote_plus(password),
                      'loginType': 'submitter'})
            self.login_token = response.json()[
                'response']['result'][0]['session']['sessionToken']
        except (requests.exceptions.HTTPError, JSONDecodeError):
            LOGGER.error(ERR_RESPONSE, response.status_code, response.content)
            LOGGER.error(ERR_AUTH, self.endpoint_new)

    def __del__(self):
        if getattr(self, 'login_token', None):
            requests.delete(
                self.endpoint_new + 'logout',
                headers={'X-Token': self.login_token})

    def retrieve_metadata(self, schema, accession):
        """
        Return XML metadata at EGA about an entity specified by accession

        Args:
            schema: AddSchema instance
            accession: str

        Returns:
            response.text

        Caution:
            all headers including auth are present in DEBUG level log output
        """
        archive = SCHEMA_ARCHIVE.get(schema, schema.value + 's')
        try:
            response = requests.get(
                self.endpoint_new + f'{archive}/{accession}'
                                     '?idtype=ega_stable_id',
                headers={'X-Token': self.login_token},
                timeout=self.timeout)
            LOGGER.debug(response.request.headers)
            LOGGER.debug(response.request.body)
            response.raise_for_status()
        # Log and raise HTTP errors
        except requests.exceptions.HTTPError as err:
            raise RequestFailed(
                ERR_RESPONSE % (response.status_code, response.content)
            ) from err
        return response.json()

    def submit_metadata(self, uploads, action, alias, receiptout):
        """
        Submit XML metadata to EGA REST API endpoint

        Args:
            uploads: list of FileUpload instances
            action: SubmissionType.Actions.Action.[Add|Validate]
            alias: short, distinctive alias for the submission
            receiptout: text buffer to write receipt response

        Caution:
            all headers including auth are present in DEBUG level log output
        """
        def action_file(upload):
            """
            Return Action element for a FileUpload
            """
            if action == Add:
                return Action(add=Add(upload.source, upload.schema))
            if action == Validate:
                return Action(validate=Validate(upload.source, upload.schema))
            raise NotImplementedError(ERR_ACTION % action)

        actions = [action_file(upload) for upload in uploads]
        actions.append(Action(protect=Protect()))
        submissionsetobj = submissionset([submission(alias, actions)])
        submissionsetdata = self.serializer.render(submissionsetobj)
        LOGGER.info(submissionsetdata)
        files = [
            (up.formname, (up.filename, up.data, 'text/plain'))
            for up in uploads
        ] + [
            ('SUBMISSION', ('SUBMISSION', submissionsetdata, 'text/plain'))
        ]

        try:
            response = requests.post(
                self.endpoint + 'submit/',
                files=files,
                auth=self.auth,
                timeout=self.timeout)
            LOGGER.debug(response.request.headers)
            LOGGER.debug(response.request.body)
            response.raise_for_status()
            receipt = etree.fromstring(response.content)
        # Log and raise HTTP errors and deserialization errors i.e. if we
        # didn't get XML back from the endpoint
        except (requests.exceptions.HTTPError, etree.XMLSyntaxError) as err:
            raise SubmissionFailed(
                ERR_RESPONSE % (response.status_code, response.content)
            ) from err

        receiptout.write(response.text)

        if receipt.attrib['success'] != 'true':
            raise SubmissionFailed(ERR_FAILED)

        LOGGER.info(MSG_SUCCEEDED)
