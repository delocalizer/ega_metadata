# pylint: disable=protected-access
"""
Convenient base class for building command-line interfaces
"""
import logging
import logging.config
import sys

from abc import ABC, abstractmethod
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, FileType

from pyhocon.exceptions import ConfigMissingException

from graflipy import logconf
from graflipy.exceptions import NotifiableError


LOGCONF = logconf.LOGCONF['filelog_1']
LOGGER = logging.getLogger(__name__)


class CLI(ABC):
    """
    Abstract base class for command-line interfaces
    """
    def __init__(self):
        # module name of the implementing class
        self.owner = type(self).__module__.split('.')[-1]
        self.parser = ArgumentParser(
            description=type(self).__doc__,
            formatter_class=ArgumentDefaultsHelpFormatter)
        self.configure_parser()
        self._configure_parser()

    def _configure_parser(self):
        """
        Append required arguments to `self.parser`
        """
        # The default logfile stem is the name of the module containing the
        # class implementation so that it matches the entrypoint name — this
        # is probably what a user expects. If you run a tool called 'add_note'
        # the associated log file is logically 'add_note.log'
        self.parser.add_argument(
            '--log-file',
            type=FileType('a'),
            default=self.owner + '.log',
            help='set the log file name')
        self.parser.add_argument(
            '--log-file-level',
            choices=logging._levelToName.values(),
            default=LOGCONF['handlers']['file']['level'],
            help='set the file handler logging level')
        self.parser.add_argument(
            '--log-stderr-level',
            choices=logging._levelToName.values(),
            default=LOGCONF['handlers']['stderr']['level'],
            help='set the stderr handler logging level')

    def _run(self, cmdline):
        """
        Run as a test article: parse the command line and call `self.work`
        """
        args = self.parser.parse_args(cmdline)
        self.work(args)
        args.log_file.close()

    def run(self):
        """
        Run as a command-line script with logging: parse arguments from
        sys.argv, call `self.work` and finally call sys.exit
        """
        args = self.parser.parse_args()
        LOGCONF['handlers']['file']['filename'] = args.log_file.name
        LOGCONF['handlers']['file']['level'] = args.log_file_level
        LOGCONF['handlers']['stderr']['level'] = args.log_stderr_level
        logging.config.dictConfig(LOGCONF)
        LOGGER.info(sys.argv)
        exit_code = 0
        try:
            self.work(args)
        # 'expected' Exceptions don't need trace; log as ERROR
        except (NotifiableError, ConfigMissingException) as problem:
            LOGGER.error(problem)
            exit_code = 100
        except Exception as ex:  # pylint: disable=broad-except
            LOGGER.exception(ex)
            exit_code = 1
        finally:
            LOGGER.info('%s exit_code: %s', self.owner, exit_code)
            args.log_file.close()
        sys.exit(exit_code)

    @abstractmethod
    def configure_parser(self):
        """
        Override this to configure `self.parser` with required args, e.g.:

            self.parser.add_argument('-f', '--foo', required=True,
                                     help='specify the foo')
        """

    @abstractmethod
    def work(self, args):
        """
        Do the work

        Args:
            args: Namespace of parsed CLI arguments
        """
