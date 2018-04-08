import unittest
from src.command_manager import CommandManager;

class CommandManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.command_manager = CommandManager()
        self.existing_commands = [
            "help",
            "version"
        ]

    def test_get_existing_command(self):
        command = self.command_manager.get_command("help")
        self.assertIsNotNone(command)

    def test_get_non_existing_command(self):
        command = self.command_manager.get_command("fudnuck")
        self.assertIsNone(command)

    def test_command_list(self):
        command_list = self.command_manager.get_command_list()
        self.assertEqual(len(command_list), len(self.existing_commands))
        for i in range(0, len(self.existing_commands) - 1):
            self.assertIsNotNone(self.command_manager.get_command(self.existing_commands[i]))
