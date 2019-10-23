import unittest
from unittest.mock import Mock

from src.t1000.application.result.events import ConsoleEventsResult, HtmlEventsResult

class ConsoleEventsResultTestCase(unittest.TestCase):
    def test_get_result_ok(self):
        command = Mock()
        resource = Mock()
        resource.get.return_value = {}
        console_event_result = ConsoleEventsResult(command, resource)
        console_event = console_event_result.get()
        self.assertEqual(console_event, ({}, 0))

    def test_get_result_ko(self):
        command = Mock()
        command.execute.side_effect = Exception('Nooooooo')
        command.set_params.return_value = command
        console_event_result = ConsoleEventsResult(command, Mock())
        console_event = console_event_result.get()
        self.assertEqual(console_event, ({}, 1))

class HtmlEventResultTestCase(unittest.TestCase):
    def test_get_result_ok(self):
        command = Mock()
        resource = Mock()
        resource.get.return_value = {}
        html_event_result = HtmlEventsResult(command, resource)
        html_event = html_event_result.get()
        self.assertEqual(html_event, ({'events': {}}, 200))

    def test_get_result_ko(self):
        command = Mock()
        command.execute.side_effect = Exception('Nooooo')
        command.set_params.return_value = command
        html_event_result = HtmlEventsResult(command, Mock())
        html_event = html_event_result.get()
        self.assertEqual(html_event, ({}, 500))
