import unittest
from src.commands.help import HelpCommand
from src.command_manager import CommandManager

class HelpCommandImplementationTestCase(unittest.TestCase):
    def setUp(self):
        self.command_manager = CommandManager()
        self.help_command = HelpCommand(self.command_manager)

    def test_get_help_is_implemented(self):
        """Test that "get_help" was implemented from the base class"""
        not_implemented = False
        try:
            self.help_command.get_help()
        except NotImplementedError:
            not_implemented = True
        self.assertFalse(not_implemented)

    def test_execute_is_implemented(self):
        """Test that "execute" was implemented from the base class"""
        not_implemented = False
        try:
            self.help_command.execute([])
        except NotImplementedError:
            not_implemented = True
        self.assertFalse(not_implemented)
