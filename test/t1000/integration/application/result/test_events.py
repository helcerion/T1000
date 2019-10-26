import unittest

from src.t1000.application.command.events import (GetEventsFromThisMonth,
                                                  GetEventsFromToday)
from src.t1000.application.resource.events import EventsDetail
from src.t1000.application.result.events import (ConsoleEventsResult,
                                                 HtmlEventsResult)
from src.t1000.domain.repository import EventsRepo
from src.t1000.infrastructure.persistence import EventsInMemoryRepo


class ConsoleEventsResultTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.resource = EventsDetail()

    def tearDown(self):
        self.resource = None
        return super().tearDown()

    def test_with_command_get_events_from_today(self):
        command = GetEventsFromToday(EventsRepo(EventsInMemoryRepo()))
        console_events_result = ConsoleEventsResult(command, self.resource)
        console_events = console_events_result.get()
        self.assertEqual(console_events, ({}, 0))

    def test_with_command_get_events_from_this_month(self):
        command = GetEventsFromThisMonth(EventsRepo(EventsInMemoryRepo()))
        console_events_result = ConsoleEventsResult(command, self.resource)
        console_events = console_events_result.get()
        self.assertEqual(console_events, ({
            '2019-10-01': [{'event_type': 'entrada', 'time': '07:20:00'},
                           {'event_type': 'salida', 'time': '14:35:00'}],
            '2019-10-15': [{'event_type': 'entrada', 'time': '07:05:30'},
                           {'event_type': 'salida', 'time': '08:05:30'},
                           {'event_type': 'entrada', 'time': '09:05:30'},
                           {'event_type': 'salida', 'time': '09:15:30'},
                           {'event_type': 'entrada', 'time': '10:05:30'}],
            '2019-10-16': [{'event_type': 'entrada', 'time': '07:05:30'}]
        }, 0))
    
    def test_with_command_get_events_from_today_setting_command_and_resource_after(self):
        command = GetEventsFromToday(EventsRepo(EventsInMemoryRepo()))
        console_events_result = ConsoleEventsResult(None, None)
        console_events_result.set_command(command)
        console_events_result.set_resource(self.resource)
        console_events = console_events_result.get()
        self.assertEqual(console_events, ({}, 0))
    
    def test_with_excetion(self):
        console_events_result = ConsoleEventsResult(None, None)
        console_events = console_events_result.get()
        self.assertEqual(console_events, ({}, 1))


class HtmlEventsResultTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.resource = EventsDetail()

    def tearDown(self):
        self.resource = None
        return super().tearDown()

    def test_with_command_get_events_from_today(self):
        command = GetEventsFromToday(EventsRepo(EventsInMemoryRepo()))
        html_events_result = HtmlEventsResult(command, self.resource)
        html_events = html_events_result.get()
        self.assertEqual(html_events, ({'events': {}}, 200))

    def test_with_command_get_events_from_this_month(self):
        resource_result = {
            '2019-10-01': [{'event_type': 'entrada', 'time': '07:20:00'},
                           {'event_type': 'salida', 'time': '14:35:00'}],
            '2019-10-15': [{'event_type': 'entrada', 'time': '07:05:30'},
                           {'event_type': 'salida', 'time': '08:05:30'},
                           {'event_type': 'entrada', 'time': '09:05:30'},
                           {'event_type': 'salida', 'time': '09:15:30'},
                           {'event_type': 'entrada', 'time': '10:05:30'}],
            '2019-10-16': [{'event_type': 'entrada', 'time': '07:05:30'}]
        }
        command = GetEventsFromThisMonth(EventsRepo(EventsInMemoryRepo()))
        html_events_result = HtmlEventsResult(command, self.resource)
        html_events = html_events_result.get()
        self.assertEqual(html_events, ({'events': resource_result}, 200))
    
    def test_with_exception(self):
        html_events_result = HtmlEventsResult(None, None)
        html_events = html_events_result.get()
        self.assertEqual(html_events, ({}, 500))
