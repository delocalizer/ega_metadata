"""
cli package entry point
"""
import pkg_resources

# for convenient imports from graflipy.cli
from graflipy.cli.cli import CLI
from graflipy.cli.exceptions import (EntityNotFound,
                                     FileExists,
                                     InvalidClass,
                                     InvalidProperty,
                                     InvalidTargetType,
                                     ParseValueError)
from graflipy.cli.report import Report
from graflipy.cli.submit import Submitter

import graflipy


def main():
    """
    Help for the user to tell them what scripts this package makes available.

    This is itself registered as a console_script entry point.
    """
    # Since this is intended for the information of end-users it deliberately
    # doesn't list entry_points from other packages e.g. graflipy.codegen
    print(f'graflipy version {graflipy.__version__}\n')
    print('This package contains the following command-line scripts:')
    for ep in pkg_resources.iter_entry_points('console_scripts'):
        if ep.module_name.startswith(__package__ + '.'):
            print(f'\t{ep.name}')
    print('\n<script> --help for help on individual scripts')
