import unittest
from unittest.mock import patch

from src.t1000.application.dependency_injection.command_factory import EventsCommandFactory


class EventsCommandFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @patch('src.t1000.application.dependency_injection.command_factory.EventsRepositoryFactory')
    def test_create_with_exception(self, repository_factory_mock):
        with self.assertRaises(Exception) as e:
            EventsCommandFactory.create('exception', '', '')
        
        self.assertEqual(str(e.exception), 'Command exception does not supported')
    
    @patch('src.t1000.application.dependency_injection.command_factory.GetEventsFromThisMonth')
    @patch('src.t1000.application.dependency_injection.command_factory.GetEventsFromToday')
    @patch('src.t1000.application.dependency_injection.command_factory.EventsRepositoryFactory')
    def test_create_from_today(self, repository_factory_mock, events_today_mock, events_month_mock):
        EventsCommandFactory.create('get_events_from_today', '', '')
        events_today_mock.assert_called_once()
        events_month_mock.assert_not_called()

    @patch('src.t1000.application.dependency_injection.command_factory.GetEventsFromThisMonth')
    @patch('src.t1000.application.dependency_injection.command_factory.GetEventsFromToday')
    @patch('src.t1000.application.dependency_injection.command_factory.EventsRepositoryFactory')
    def test_create_this_month(self, repository_factory_mock, events_today_mock, events_month_mock):
        EventsCommandFactory.create('get_events_this_month', '', '')
        events_month_mock.assert_called_once()
        events_today_mock.assert_not_called()
