# Implementation of the help command

from src.commands.abstract_command import AbstractCommand
from src.utilities.print_formatter import PrintFormatter as PF
from src.utilities.print_formatter import Color

class HelpCommand(AbstractCommand):
    """docstring for HelpCommand."""
    def __init__(self, command_manager):
        super(HelpCommand, self).__init__()
        self.name = "help";
        self.description = "Display help about possible commands"
        self.command_manager = command_manager

    def list_commands(self):
        """Return a string listing possible commands along with their short description"""
        list_str = "General usage: " + Color.BOLD + "./orchid [COMMAND [OPTIONS] [ARGS]]" + Color.END
        list_str += "\nSupported commands:"
        for key in self.command_manager.get_command_list():
            description = self.command_manager.get_command(key).get_description()
            list_str += ("\n   " + Color.BOLD + "{0:12}" + Color.END + " {1}").format(key, description)
        list_str += "\nType " + Color.BOLD + "./orchid help [COMMAND]" + Color.END + " for more advanced usage information"
        return list_str

    def get_help(self):
        """Return the detailed help about the "help" command options and usage."""
        return (PF.title("Help command manual")
             + PF.section("Description")
             + PF.paragraph(self.description)
             + PF.section("Synopsis")
             + PF.paragraph(Color.BOLD + "./orchid help [COMMAND]" + Color.END)
             + PF.section("Description")
             + PF.paragraph("With no " + Color.BOLD + "COMMAND" + Color.END + " specified, print available commands on the standard output.")
             + PF.paragraph("If " + Color.BOLD + "COMMAND" + Color.END + " is specified and exists, print the help manual of the command on the standard output."))

    def execute(self, argv):
        if len(argv) == 0:
            print(self.list_commands())
        else:
            # Get the command from the arguments
            command_name = argv[0]
            command = self.command_manager.get_command(command_name)
            if command == None:
                print("No help available for unknown command \"" + command_name + "\"")
            else:
                print(command.get_help())
