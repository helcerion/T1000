import unittest
from unittest.mock import Mock

from src.t1000.application.command.events import GetEventsFromToday


class GetEventsFromTodayTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_set_params_return_self(self):
        command_get_from_today = GetEventsFromToday(Mock())
        command_returned = command_get_from_today.set_params()
        self.assertEqual(command_get_from_today, command_returned)

    def test_execute(self):
        repo_mock = Mock()
        command_get_from_today = GetEventsFromToday(repo_mock)
        command_get_from_today.execute()
        repo_mock.get_from_today.assert_called_once()
