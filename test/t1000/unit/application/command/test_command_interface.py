import unittest
from unittest.mock import Mock

from src.t1000.application.command.command_interface import CommandInterface


class CommandInterfaceTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_implements_without_implement_execute_method(self):
        command_no_execute = CommandNoExecute(Mock)
        with self.assertRaises(Exception) as command_interface_execption:
            command_no_execute.execute()

        self.assertEqual(str(command_interface_execption.exception), \
            'You need to implement execute function from CommandNoExecute.')

    def test_set_params_return_it_self(self):
        command_no_execute = CommandNoExecute(Mock)
        command_returned = command_no_execute.set_params()
        self.assertEqual(command_no_execute, command_returned)

class CommandNoExecute(CommandInterface):
    pass