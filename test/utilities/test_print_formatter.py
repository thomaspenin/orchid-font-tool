import unittest
from src.utilities.print_formatter import PrintFormatter
from src.utilities.print_formatter import Color;

class PublicPrintFormatter(PrintFormatter):
    """Public class to test PrintFormatter private methods"""

    def __init__(self, arg):
        super(PublicPrintFormatter, self).__init__()
        self.arg = arg

    @staticmethod
    def public_remove_format_marks(str):
        return PrintFormatter._remove_format_marks(str)

    @staticmethod
    def public_remove_line_breaks(str):
        return PrintFormatter._remove_line_breaks(str)


class PrintFormatterTestCase(unittest.TestCase):

    # Test _remove_line_breaks

    def test_remove_line_breaks_remove(self):
        """Test that the method actually removes line breaks"""
        test_str = "\ntest\n\n bold\n str"
        clean_str = PublicPrintFormatter.public_remove_line_breaks(test_str)
        self.assertEqual(clean_str, "test bold str")

    def test_remove_line_breaks_removes_leading_trailing_spaces(self):
        """Test that the method removes leading and trailing spaces"""
        test_str = "     test bold str      "
        clean_str = PublicPrintFormatter.public_remove_line_breaks(test_str)
        self.assertEqual(clean_str, "test bold str")

    def test_remove_line_breaks_preserves_string(self):
        """Test that the method preserves strings without line breaks, leading or trailing spaces"""
        test_str = "test bold str"
        clean_str = PublicPrintFormatter.public_remove_line_breaks(test_str)
        self.assertEqual(clean_str, "test bold str")

    # Test _remove_format_marks

    def test_remove_format_mark_bold(self):
        """Test that the method to remove format marks works with bold"""
        test_str = "test " + Color.BOLD + "bold" + Color.END + " str"
        clean_str = PublicPrintFormatter.public_remove_format_marks(test_str)
        self.assertEqual(clean_str, "test bold str")

    def test_remove_format_mark_no_mark(self):
        """Test that the method to remove format marks leaves str untouched when nothing to do"""
        test_str = "test clean str"
        clean_str = PublicPrintFormatter.public_remove_format_marks(test_str)
        self.assertEqual(clean_str, test_str)
        test_str2 = ""
        clean_str2 = PublicPrintFormatter.public_remove_format_marks(test_str2)
        self.assertEqual(clean_str2, test_str2)

    # Test title

    def test_title_line_breaks(self):
        """Test that the result begins and ends with a line break"""
        test_str = "test str"
        formatted_str = PrintFormatter.title(test_str)
        str_length = len(formatted_str)
        self.assertTrue(str_length > 2)
        self.assertEqual(formatted_str[0], '\n')
        self.assertEqual(formatted_str[str_length - 1], '\n')

    def test_title_is_bold(self):
        """Test that the result format is surrounded by bold commands"""
        test_str = "test str"
        formatted_str = PrintFormatter.title(test_str)
        str_length = len(formatted_str)
        self.assertTrue(str_length > 8)
        self.assertEqual(formatted_str.find('\033[1m'), 1)
        self.assertEqual(formatted_str.find('\033[0m'), str_length - 5)

    def test_title_is_upper(self):
        """Test that the content to format is kept as upper case"""
        test_str = "test str"
        formatted_str = PrintFormatter.title(test_str)
        self.assertEqual(formatted_str.count(test_str.upper()), 1)

    def test_title_empty_string(self):
        """Test that the result is an empty string for an empty string"""
        test_str = ""
        formatted_str = PrintFormatter.title(test_str)
        self.assertEqual(formatted_str, "")

    def test_title_containing_formatting(self):
        """Test that title is correct when there was already formatting marks
           (internal formatting shall be removed)
        """
        test_str = "test " + Color.BOLD + "bold" + Color.END + " str"
        formatted_str = PrintFormatter.title(test_str)
        self.assertEqual(formatted_str, "\n\033[1mTEST BOLD STR\033[0m\n")

    def test_title_removes_inner_line_breaks(self):
        """Test that inner line breaks are removed"""
        test_str = "test\nbroken\nstr"
        formatted_str = PrintFormatter.title(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "\n\033[1mTEST BROKEN STR\033[0m\n")

    # Test section

    def test_section_line_breaks(self):
        """Test that the result begins and ends with a line break"""
        test_str = "test str"
        formatted_str = PrintFormatter.section(test_str)
        str_length = len(formatted_str)
        self.assertTrue(str_length > 2)
        self.assertEqual(formatted_str[0], '\n')
        self.assertEqual(formatted_str[str_length - 1], '\n')

    def test_section_is_bold(self):
        """Test that the result format is surrounded by bold commands"""
        test_str = "test str"
        formatted_str = PrintFormatter.section(test_str)
        str_length = len(formatted_str)
        self.assertTrue(str_length > 8)
        self.assertEqual(formatted_str.find('\033[1m'), 1)
        self.assertEqual(formatted_str.find('\033[0m'), str_length - 5)

    def test_section_is_upper(self):
        """Test that the content to format is kept as upper case"""
        test_str = "test str"
        formatted_str = PrintFormatter.section(test_str)
        self.assertEqual(formatted_str.count(test_str.upper()), 1)

    def test_section_empty_string(self):
        """Test that the result is an empty string for an empty string"""
        test_str = ""
        formatted_str = PrintFormatter.section(test_str)
        self.assertEqual(formatted_str, "")

    def test_section_containing_formatting(self):
        """Test that title is correct when there was already formatting marks
           (internal formatting shall be removed)
        """
        test_str = "test " + Color.BOLD + "bold" + Color.END + " str"
        formatted_str = PrintFormatter.section(test_str)
        self.assertEqual(formatted_str, "\n\033[1mTEST BOLD STR\033[0m\n")

    def test_section_removed_inner_line_breaks(self):
        """Test that inner line breaks are removed"""
        test_str = "test\nbroken\nstr"
        formatted_str = PrintFormatter.section(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "\n\033[1mTEST BROKEN STR\033[0m\n")

    # Test paragraph

    def test_paragraph_line_breaks(self):
        """Test that the result begins and ends with a line break"""
        test_str = "test str"
        formatted_str = PrintFormatter.paragraph(test_str)
        str_length = len(formatted_str)
        self.assertTrue(str_length > 2)
        self.assertEqual(formatted_str[0], '\n')
        self.assertEqual(formatted_str[str_length - 1], '\n')

    def test_paragraph_is_indented(self):
        """Test that the result format is properly indented"""
        test_str = "test str"
        formatted_str = PrintFormatter.paragraph(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "\n    test str\n")

    def test_paragraph_empty_string(self):
        """Test that the result is an empty string for an empty string"""
        test_str = ""
        formatted_str = PrintFormatter.paragraph(test_str)
        self.assertEqual(formatted_str, "")

    def test_paragraph_containing_formatting(self):
        """Test that internal formatting marks are preserved"""
        test_str = "test " + Color.BOLD + "bold" + Color.END + " str"
        formatted_str = PrintFormatter.paragraph(test_str)
        self.assertEqual(formatted_str, "\n    test \033[1mbold\033[0m str\n")

    def test_paragraph_removes_internal_line_breaks(self):
        """Test that inner line breaks are replaced by spaces"""
        test_str = "test\nbroken\nstr"
        formatted_str = PrintFormatter.paragraph(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "\n    test broken str\n")

    def test_paragraph_preserves_capitalization(self):
        """Test that capitalization is preserved"""
        test_str = "tEst brOKen str"
        formatted_str = PrintFormatter.paragraph(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "\n    tEst brOKen str\n")

    # Test paragraphsub

    def test_paragraphsub_ends_with_line_breaks(self):
        """Test that the result ends with a line break"""
        test_str = "test str"
        formatted_str = PrintFormatter.paragraphsub(test_str)
        str_length = len(formatted_str)
        self.assertTrue(str_length > 2)
        self.assertEqual(formatted_str[str_length - 1], '\n')

    def test_paragraphsub_is_indented(self):
        """Test that the result format is properly indented"""
        test_str = "test str"
        formatted_str = PrintFormatter.paragraphsub(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "        test str\n")

    def test_paragraphsub_empty_string(self):
        """Test that the result is an empty string for an empty string"""
        test_str = ""
        formatted_str = PrintFormatter.paragraphsub(test_str)
        self.assertEqual(formatted_str, "")

    def test_paragraphsub_containing_formatting(self):
        """Test that internal formatting marks are preserved"""
        test_str = "test " + Color.BOLD + "bold" + Color.END + " str"
        formatted_str = PrintFormatter.paragraphsub(test_str)
        self.assertEqual(formatted_str, "        test \033[1mbold\033[0m str\n")

    def test_paragraphsub_removes_internal_line_breaks(self):
        """Test that inner line breaks are replaced by spaces"""
        test_str = "test\nbroken\nstr"
        formatted_str = PrintFormatter.paragraphsub(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "        test broken str\n")

    def test_paragraphsub_preserves_capitalization(self):
        """Test that capitalization is preserved"""
        test_str = "tEst brOKen str"
        formatted_str = PrintFormatter.paragraphsub(test_str)
        str_length = len(formatted_str)
        self.assertEqual(formatted_str, "        tEst brOKen str\n")
