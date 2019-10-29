import unittest
from unittest.mock import patch

from src.t1000.application.dependency_injection.result_factory import EventsResultFactory


class EventsResultFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @patch('src.t1000.application.dependency_injection.result_factory.HtmlEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.ConsoleEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsCommandFactory')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsResourceFactory')
    def test_create_with_resource_exception(self, resource_mock, command_mock, console_mock, html_mock):
        resource_mock.create.side_effect = Exception('Raise exception')
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'exception', 'exception', 'exception', 'exception')

        self.assertEqual(str(e.exception), 'Raise exception')
        resource_mock.create.assert_called_once_with('exception')
        command_mock.create.assert_not_called()
        console_mock.assert_not_called()
        html_mock.assert_not_called()

    @patch('src.t1000.application.dependency_injection.result_factory.HtmlEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.ConsoleEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsCommandFactory')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsResourceFactory')
    def test_create_with_command_exception(self, resource_mock, command_mock, console_mock, html_mock):
        command_mock.create.side_effect = Exception('Raise exception')
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'events_detail', 'exception', 'Events', 'in_memory')

        self.assertEqual(str(e.exception), 'Raise exception')
        resource_mock.create.assert_called_once_with('events_detail')
        command_mock.create.assert_called_once_with(use_case='exception', entity='Events', persistence_type='in_memory')
        console_mock.assert_not_called()
        html_mock.assert_not_called()

    @patch('src.t1000.application.dependency_injection.result_factory.HtmlEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.ConsoleEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsCommandFactory')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsResourceFactory')
    def test_create_with_exception(self, resource_mock, command_mock, console_mock, html_mock):
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'events_detail', 'get_events_from_today', 'Events', 'in_memory')

        self.assertEqual(str(e.exception), 'Result type exception does not supported')
        resource_mock.create.assert_called_once_with('events_detail')
        command_mock.create.assert_called_once_with(use_case='get_events_from_today', entity='Events', persistence_type='in_memory')
        console_mock.assert_not_called()
        html_mock.assert_not_called()

    @patch('src.t1000.application.dependency_injection.result_factory.HtmlEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.ConsoleEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsCommandFactory')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsResourceFactory')
    def test_create_cmd(self, resource_mock, command_mock, console_mock, html_mock):
        EventsResultFactory.create('cmd', 'events_detail', 'get_events_from_today', 'Events', 'in_memory')
        resource_mock.create.assert_called_once_with('events_detail')
        command_mock.create.assert_called_once_with(use_case='get_events_from_today', entity='Events', persistence_type='in_memory')
        console_mock.assert_called_once()
        html_mock.assert_not_called()

    @patch('src.t1000.application.dependency_injection.result_factory.HtmlEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.ConsoleEventsResult')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsCommandFactory')
    @patch('src.t1000.application.dependency_injection.result_factory.EventsResourceFactory')
    def test_create_html(self, resource_mock, command_mock, console_mock, html_mock):
        EventsResultFactory.create('html', 'events_detail', 'get_events_from_today', 'Events', 'in_memory')
        resource_mock.create.assert_called_once_with('events_detail')
        command_mock.create.assert_called_once_with(use_case='get_events_from_today', entity='Events', persistence_type='in_memory')
        console_mock.assert_not_called()
        html_mock.assert_called_once()
