import textwrap
import re

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class PrintFormatter(object):
    """docstring for PrintFormatter."""
    def __init__(self):
        super(HelpFormatter, self).__init__()

    @staticmethod
    def title(title_str):
        if title_str == "":
            return ""
        else:
            return "\n" + Color.BOLD + PrintFormatter._remove_format_marks(PrintFormatter._remove_line_breaks(title_str)).upper() + Color.END + "\n"

    @staticmethod
    def section(section_str):
        if section_str == "":
            return ""
        else:
            return "\n" + Color.BOLD + PrintFormatter._remove_format_marks(PrintFormatter._remove_line_breaks(section_str)).upper() + Color.END + "\n"

    @staticmethod
    def paragraph(paragraph_str):
        if paragraph_str == "":
            return ""
        else:
            return "\n" + textwrap.fill(paragraph_str, initial_indent='    ', subsequent_indent='    ') + "\n"

    @staticmethod
    def paragraphsub(paragraph_str):
        if paragraph_str == "":
            return ""
        else:
            return textwrap.fill(paragraph_str, initial_indent='        ', subsequent_indent='        ') + "\n"

    @staticmethod
    def _remove_format_marks(str):
        """Remove all shell format marks from the string in parameter"""
        str2 = str
        str2 = str2.replace(Color.PURPLE, "")
        str2 = str2.replace(Color.CYAN, "")
        str2 = str2.replace(Color.DARKCYAN, "")
        str2 = str2.replace(Color.BLUE, "")
        str2 = str2.replace(Color.GREEN, "")
        str2 = str2.replace(Color.YELLOW, "")
        str2 = str2.replace(Color.RED, "")
        str2 = str2.replace(Color.BOLD, "")
        str2 = str2.replace(Color.UNDERLINE, "")
        str2 = str2.replace(Color.END, "")
        return str2

    @staticmethod
    def _remove_line_breaks(str):
        """Removes all line breaks and replace those inside the string by one space at most"""
        str2 = str
        str2 = str2.replace("\n", " ")     # Replace line breaks
        str2 = str2.strip()                # Remove leading and trailing spaces
        str2 = re.sub('\s{2,}', ' ', str2) # At most one space
        return str2
