"""
Prepare ANALYSIS.xml metadata describing bams transferred to EGA.
"""
from argparse import FileType

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from graflipy import configure
from graflipy.cli import CLI
from graflipy.ega import study_accession
from graflipy.ega.metadata import analysisset
from graflipy.ega.schema_1_5_0 import ANALYSISXSD
from graflipy.envconf import ENVS
from graflipy.reference import ReferenceAssembly

XMLCONF = SerializerConfig(pretty_print=True,
                           no_namespace_schema_location=ANALYSISXSD)


class EGAAnalysisXML(CLI):
    """
    Prepare ANALYSIS.xml metadata describing bams transferred to EGA.
    """

    def configure_parser(self):
        """
        Configure `self.parser` with required args
        """
        default_output = 'ANALYSIS.xml'
        references = sorted(ref.name for ref in ReferenceAssembly.values)
        self.parser.add_argument('-e', dest='environment', required=True,
                                 choices=ENVS)
        self.parser.add_argument('-i', '--input', required=True, dest='paths',
                                 action='append', metavar='PATH',
                                 help='path to original (unencrypted) bam: '
                                 'specify multiple times for multiple bams')
        self.parser.add_argument('-o', '--output', type=FileType('w'),
                                 metavar='PATH', default=default_output,
                                 help='use - for stdout')
        self.parser.add_argument('--checksum-files-dir', required=True,
                                 metavar='PATH',
                                 help='directory containing the [bam].md5 and '
                                 '[bam].gpg.md5 files for all input bams')
        self.parser.add_argument('--ega-submission-dir', required=True,
                                 metavar='PATH',
                                 help='directory at EGA box into which the '
                                 'encrypted files will be/have been submitted')
        self.parser.add_argument('--study-ref-accession', required=True,
                                 type=study_accession,
                                 metavar='EGASXXXXXXXXXXX')
        self.parser.add_argument('--include-accessioned', action='store_true',
                                 help='include analyses that already have an '
                                 'accession recorded in the database')
        self.parser.add_argument('--no-db-reference', choices=references,
                                 help='if this option is supplied then the '
                                 'database is not queried for any metadata. '
                                 'The output XML is incomplete and invalid. '
                                 'This option may be useful to build scaffold '
                                 'metadata for hand-editing when bams are not '
                                 'in the database.')

    def work(self, args):
        configure(args.environment, 'READONLY')
        xmlobj = analysisset(
            args.paths,
            args.checksum_files_dir,
            args.study_ref_accession,
            args.ega_submission_dir,
            (args.no_db_reference and ReferenceAssembly.fromstr(
                args.no_db_reference)),
            args.include_accessioned)
        XmlSerializer(config=XMLCONF).write(args.output, xmlobj)


def main():
    """
    Run as a command-line script
    """
    EGAAnalysisXML().run()
