
from src.commands.help import HelpCommand
from src.commands.version import VersionCommand

class CommandManager(object):
    """docstring for CommandManager."""
    def __init__(self):
        super(CommandManager, self).__init__()
        self.command_list = self._build_command_list()

    def _build_command_list(self):
        """Build the list of available commands

        Returns:
            A dictionnary, which key is the string naming the command and the value
            the command itself
        """
        return {
            "help": HelpCommand(self),
            "version": VersionCommand()
        }

    def get_command_list(self):
        return self.command_list

    def get_command(self, name):
        try:
            return self.command_list[name]
        except KeyError:
            return None
