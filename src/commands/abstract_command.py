# Base class for commands

class AbstractCommand(object):
    """Abstract base class for commands"""
    def __init__(self):
        super(AbstractCommand, self).__init__()
        self.name = None;
        self.description = None;

    def execute(self, argv):
        """Execute the command. Has to be reimplemented by subclasses"""
        raise NotImplementedError

    def get_name(self):
        """Return the name of the command, as called from command line"""
        return self.name

    def get_description(self):
        """Return a short, one-line description of the command"""
        return self.description

    def get_help(self):
        """Return the detailed help about the command options and usage.
           Has to be reimplemented by subclasses
        """
        raise NotImplementedError

    def _parse_arguments(self, arguments):
        """Method to parse command arguments

        Returns:
            TODO
        """
        raise NotImplementedError
