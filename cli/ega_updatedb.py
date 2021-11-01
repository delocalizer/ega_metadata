"""
From EGA submission receipt file, update accessions of samples & bams in grafli
"""

from argparse import FileType

from graflipy import configure
from graflipy.cli import CLI
from graflipy.ega import update_accessions
from graflipy.envconf import ENVS


class EGAUpdateDb(CLI):
    """
    From EGA submission receipt file, update accessions of samples & bams in
    grafli
    """

    def configure_parser(self):
        """
        Configure `self.parser` with required args
        """
        self.parser.add_argument('-e', dest='environment', required=True,
                                 choices=ENVS)
        self.parser.add_argument('-x', '--receipt-xml', required=True,
                                 metavar='PATH', type=FileType('rb'),
                                 help='the receipt XML from a submission '
                                 'containing ANALYSIS and/or SAMPLE elements '
                                 'with "alias" attribute')

    def work(self, args):
        configure(args.environment, 'READWRITE')
        update_accessions(args.receipt_xml)


def main():
    """
    Run as a command-line script
    """
    EGAUpdateDb().run()
