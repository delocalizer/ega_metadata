"""
Prepare DATASET.xml metadata describing a new dataset consisting of analyses
at EGA
"""
from argparse import FileType

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from graflipy.cli import CLI
from graflipy.ega import analysis_accession, policy_accession
from graflipy.ega.metadata import dataset_analysisref, datasets
from graflipy.ega.schema_1_5_0 import DATASETXSD
from graflipy.util import get_tag_attribute

XMLCONF = SerializerConfig(pretty_print=True,
                           no_namespace_schema_location=DATASETXSD)


class EGADatasetXML(CLI):
    """
    Prepare DATASET.xml metadata describing a new dataset consisting of
    analyses at EGA
    """

    def configure_parser(self):
        """
        Configure `self.parser` with required args
        """
        default_output = 'DATASET.xml'
        self.parser.epilog = ('Either --analysis-receipt or a list of '
                              '--analysis accessions may be specified')
        inputs = self.parser.add_mutually_exclusive_group(required=True)
        inputs.add_argument('-x', '--analysis-receipt', type=FileType('r'),
                            metavar='PATH',
                            help='the receipt XML from an analysis submission '
                            'containing ANALYSIS elements with accession='
                            '"<EGAZXXXXXXXXXXX>"')
        inputs.add_argument('-s', '--analysis', action='append',
                            dest='analyses', type=analysis_accession,
                            metavar='EGAZXXXXXXXXXXX')
        self.parser.add_argument('-o', '--output', type=FileType('w'),
                                 metavar='PATH', default=default_output,
                                 help='use - for stdout')
        self.parser.add_argument('-a', '--alias', required=True,
                                 help='short, distinctive alias for the '
                                 'dataset, e.g "20210303_EGA_Melanoma"')
        self.parser.add_argument('-t', '--title', required=True,
                                 help='title for the dataset, e.g. '
                                 '"20210303_EGA_Melanoma Garg et al Nat '
                                 'Commun, 2021"')
        self.parser.add_argument('-d', '--description', required=True,
                                 help='description for the dataset, e.g '
                                 '"RNAseq of 55 melanoma tumors that were '
                                 'used as a validation dataset in Garg et al '
                                 'Nat Commun, 2021 Feb 18;12(1):1137. doi: '
                                 '10.1038/s41467-021-21207-2."')
        policy = self.parser.add_mutually_exclusive_group(required=True)
        policy.add_argument('--icgc', action='store_true',
                            help='ICGC project (will be covered by existing '
                            'ICGC data access policy)')
        policy.add_argument('--policy-accession', type=policy_accession,
                            help='required if --icgc is not specified')

    def work(self, args):
        analyses = (args.analyses or get_tag_attribute(
            args.analysis_receipt, 'ANALYSIS', 'accession'))
        xmlobj = datasets([
            dataset_analysisref(
                args.alias,
                args.title,
                args.description,
                analyses,
                args.policy_accession,
                args.icgc
            )
        ])
        XmlSerializer(config=XMLCONF).write(args.output, xmlobj)


def main():
    """
    Run as a command-line script
    """
    EGADatasetXML().run()
