"""
Prepare SAMPLE.xml metadata describing samples used in submitted analyses.
"""
from argparse import FileType

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from graflipy import configure
from graflipy.cli import CLI
from graflipy.ega.metadata import sampleset
from graflipy.ega.schema_1_5_0 import SAMPLEXSD
from graflipy.envconf import ENVS
from graflipy.util import get_tag_attribute

XMLCONF = SerializerConfig(pretty_print=True,
                           no_namespace_schema_location=SAMPLEXSD)


class EGASampleXML(CLI):
    """
    Prepare SAMPLE.xml metadata describing samples used in submitted analyses.
    """

    def configure_parser(self):
        """
        Configure `self.parser` with required args
        """
        default_output = 'SAMPLE.xml'
        self.parser.epilog = ('Either --analysis-xml or a list of --sample '
                              'uuids may be specified')
        self.parser.add_argument('-e', dest='environment', required=True,
                                 choices=ENVS)
        inputs = self.parser.add_mutually_exclusive_group(required=True)
        inputs.add_argument('-x', '--analysis-xml', metavar='PATH',
                            type=FileType('r'),
                            help='prepared ANALYSIS.xml file, containing '
                            'SAMPLE_REF elements with refname="<uuid>"')
        inputs.add_argument('-s', '--sample', action='append', dest='samples',
                            metavar='UUID')
        self.parser.add_argument('-o', '--output', type=FileType('w'),
                                 metavar='PATH', default=default_output,
                                 help='use - for stdout')
        self.parser.add_argument('--include-accessioned', action='store_true',
                                 help='include samples that already have an '
                                 'accession recorded in the database')

    def work(self, args):
        configure(args.environment, 'READONLY')
        samples = (args.samples or get_tag_attribute(
            args.analysis_xml, 'SAMPLE_REF', 'refname'))
        xmlobj = sampleset(samples, args.include_accessioned)
        XmlSerializer(config=XMLCONF).write(args.output, xmlobj)


def main():
    """
    Run as a command-line script
    """
    EGASampleXML().run()
