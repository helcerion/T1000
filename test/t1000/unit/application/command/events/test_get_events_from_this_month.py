import unittest
from unittest.mock import Mock

from src.t1000.application.command.events import GetEventsFromThisMonth


class GetEventsFromThisMonthTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_set_params_return_self(self):
        command_get_events_from_this_month = GetEventsFromThisMonth(Mock())
        command_returned = command_get_events_from_this_month.set_params()
        self.assertEqual(command_get_events_from_this_month, command_returned)

    def test_execute(self):
        repo_mock = Mock()
        command_get_events_from_this_month = GetEventsFromThisMonth(repo_mock)
        command_get_events_from_this_month.execute()
        repo_mock.get_month.assert_called_once()
