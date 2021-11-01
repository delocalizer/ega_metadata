"""
Submit metadata to EGA, with either ADD or VALIDATE action
"""
from argparse import FileType

from graflipy import get_config
from graflipy.cli import CLI
from graflipy.ega.client import FileUpload, RESTClient
from graflipy.ega.schema_1_5_0 import AddSchema, SubmissionType

EGACONF = get_config().ega
ADD = SubmissionType.Actions.Action.Add
VALIDATE = SubmissionType.Actions.Action.Validate


class EGASubmitXML(CLI):
    """
    Submit metadata to EGA, with either ADD or VALIDATE action
    """

    def configure_parser(self):
        """
        Configure `self.parser` with required args
        """
        default_output = 'RECEIPT.xml'
        default_ega_account = EGACONF.accountName
        self.parser.add_argument('-a', '--alias',
                                 help='short, distinctive alias for the '
                                 'submission, e.g "<initials> `date`"')
        self.parser.add_argument('--ega-account', default=default_ega_account,
                                 help='submission account')
        self.parser.add_argument('--ega-password-file', required=True,
                                 type=FileType('r'))
        actions = self.parser.add_mutually_exclusive_group(required=True)
        actions.add_argument('--add', action='store_true',
                             help='ADD the metadata')
        actions.add_argument('--validate', action='store_true',
                             help='VALIDATE the metadata')
        self.parser.add_argument('--schema-analysis-file', type=FileType('r'),
                                 help='path to ANALYSIS.xml')
        self.parser.add_argument('--schema-dataset-file', type=FileType('r'),
                                 help='path to DATASET.xml')
        self.parser.add_argument('--schema-sample-file', type=FileType('r'),
                                 help='path to SAMPLE.xml')
        self.parser.add_argument('-o', '--output', type=FileType('w'),
                                 metavar='PATH', default=default_output,
                                 help='use - for stdout')
        self.parser.add_argument('--test', action='store_true',
                                 help='Submit to test server; metadata is '
                                 'deleted after 24hrs')

    def work(self, args):
        if not (args.schema_analysis_file or args.schema_dataset_file or
                args.schema_sample_file):
            self.parser.error('No schema file specified')
        client = RESTClient(args.ega_account,
                            password_file=args.ega_password_file.name,
                            test=args.test)
        uploads = []
        if args.schema_analysis_file:
            uploads.append(
                FileUpload(AddSchema.ANALYSIS, args.schema_analysis_file))
        if args.schema_dataset_file:
            uploads.append(
                FileUpload(AddSchema.DATASET, args.schema_dataset_file))
        if args.schema_sample_file:
            uploads.append(
                FileUpload(AddSchema.SAMPLE, args.schema_sample_file))
        client.submit_metadata(
            uploads,
            ADD if args.add else VALIDATE,
            args.alias,
            args.output)


def main():
    """
    Run as a command-line script
    """
    EGASubmitXML().run()
