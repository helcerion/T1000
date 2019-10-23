import unittest

from src.t1000.application.resource.events import EventsDetail
from src.t1000.domain.entity import Event, Events

class EventsDetailTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.events_detail = EventsDetail()

    def tearDown(self):
        self.events_detail = None
        return super().tearDown()

    def test_without_events(self):
        events_entity = Events([])
        self.events_detail.set(events_entity)
        events = self.events_detail.get()
        self.assertEqual(events, {})

    def test_with_only_one_event(self):
        event_entity = Event('asdf', '2019-10-19', '07:05:00', 'entrada')
        events_entity = Events([event_entity])
        self.events_detail.set(events_entity)
        events = self.events_detail.get()
        result = {'2019-10-19': [{'event_type': 'entrada', 'time': '07:05:00'}]}
        self.assertEqual(events, result)

    def test_with_two_events_different_data(self):
        event_entity_1 = Event('asd', '2019-10-19', '07:05:00', 'entrada')
        event_entity_2 = Event('asf', '2019-10-18', '07:05:00', 'entrada')
        events_entity = Events([event_entity_1, event_entity_2])
        self.events_detail.set(events_entity)
        events = self.events_detail.get()
        result = {'2019-10-19': [{'event_type': 'entrada', 'time': '07:05:00'}],
            '2019-10-18': [{'event_type': 'entrada', 'time': '07:05:00'}]}
        self.assertEqual(events, result)

    def test_with_two_events_same_data(self):
        event_entity_1 = Event('asd', '2019-10-19', '07:05:00', 'entrada')
        event_entity_2 = Event('asf', '2019-10-19', '14:05:00', 'salida')
        events_entity = Events([event_entity_1, event_entity_2])
        self.events_detail.set(events_entity)
        events = self.events_detail.get()
        result = {'2019-10-19': [{'event_type': 'entrada', 'time': '07:05:00'},
            {'event_type': 'salida', 'time': '14:05:00'}]}
        self.assertEqual(events, result)
