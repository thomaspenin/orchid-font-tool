# Implementation of the "version" command

from src.commands.abstract_command import AbstractCommand
from src.utilities.print_formatter import PrintFormatter as PF
from src.utilities.print_formatter import Color
import json

class VersionCommand(AbstractCommand):
    """docstring for VersionCommand."""
    def __init__(self):
        super(VersionCommand, self).__init__()
        self.name = "version"
        self.description = "Display version information"

    def get_help(self):
        return (PF.title("Version command manual")
             + PF.section("Description")
             + PF.paragraph(self.description)
             + PF.section("Synopsis")
             + PF.paragraph(Color.BOLD + "./orchid version [-t|--tool|-f|--font]" + Color.END)
             + PF.section("Description")
             + PF.paragraph("With no option specified, print the version of the tool on the standard output.")
             + PF.paragraph("Options allow specifying if the latest version of the tool or that of the font is to be displayed.")
             + PF.section("Options")
             + PF.paragraph("-t, --tool")
             + PF.paragraphsub("Print the version of the Orchid Font Tool.")
             + PF.paragraph("-f, --font")
             + PF.paragraphsub("Print the version of the Orchid Font."))

    def execute(self, argv):
        if len(argv) == 0 or (len(argv) == 1 and (argv[0] == "-t" or argv[0] == "--tool")):
            with open('info.json') as json_data:
                d = json.load(json_data)
                print(d["tool-version"])
        elif len(argv) == 1 and (argv[0] == "-f" or argv[0] == "--font"):
            # TODO: use config instead of hard-coded path and check file is available
            with open('../orchid-font/info.json') as json_data:
                d = json.load(json_data)
                print(d["version"])
        else:
            print("Unknown arguments. Type " + Color.BOLD + "./orchid help version" + Color.END + " for usage instructions.")
