import unittest
from src.commands.version import VersionCommand

class VersionCommandImplementationTestCase(unittest.TestCase):
    def setUp(self):
        self.version_command = VersionCommand()

    def test_get_help_is_implemented(self):
        """Test that "get_help" was implemented from the base class"""
        not_implemented = False
        try:
            self.version_command.get_help()
        except NotImplementedError:
            not_implemented = True
        self.assertFalse(not_implemented)

    def test_execute_is_implemented(self):
        """Test that "execute" was implemented from the base class"""
        not_implemented = False
        try:
            self.version_command.execute([])
        except NotImplementedError:
            not_implemented = True
        self.assertFalse(not_implemented)
