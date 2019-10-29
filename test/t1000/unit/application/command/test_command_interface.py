import unittest
from unittest.mock import Mock

from src.t1000.application.command.command_abstract import CommandAbstract


class CommandAbstractTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_implements_without_implement_execute_method(self):
        command_no_execute = CommandNoExecute(Mock)
        with self.assertRaises(Exception) as command_abstract_execption:
            command_no_execute.execute()

        self.assertEqual(str(command_abstract_execption.exception), \
            'You need to implement execute function from CommandNoExecute.')


class CommandNoExecute(CommandAbstract):
    pass