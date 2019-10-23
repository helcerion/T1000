import unittest
from typing import List
from unittest.mock import Mock, PropertyMock, patch

from src.t1000.application.resource.events import EventsDetail
from src.t1000.domain.entity import Event


class EventsDetailTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.events_detail = EventsDetail()

    def tearDown(self):
        self.events_detail = None
        return super().tearDown()

    def test_without_events(self):
        events_mock = Mock(events=[])
        self.events_detail.set(events_mock)
        events = self.events_detail.get()
        self.assertEqual(events, {})

    def test_with_only_one_event(self):
        event_mock = Mock(date='2019-10-19', time='12:10:30', event_type='entrada')
        events_mock = Mock(events=[event_mock])
        self.events_detail.set(events_mock)
        events = self.events_detail.get()
        result = {'2019-10-19': [{'event_type': 'entrada', 'time': '12:10:30'}]}
        self.assertEqual(events, result)

    def test_with_two_events_different_data(self):
        event_mock_1 = Mock(date='2019-10-18', time='12:10:30', event_type='entrada')
        event_mock_2 = Mock(date='2019-10-19', time='07:20:02', event_type='entrada')
        events_mock = Mock(events=[event_mock_1, event_mock_2])
        self.events_detail.set(events_mock)
        events = self.events_detail.get()
        result = {
            '2019-10-18': [{'event_type': 'entrada', 'time': '12:10:30'}],
            '2019-10-19': [{'event_type': 'entrada', 'time': '07:20:02'}]}
        self.assertEqual(events, result)

    def test_with_two_events_same_data(self):
        event_mock_1 = Mock(date='2019-10-18', event_type='entrada', time='07:10:21')
        event_mock_2 = Mock(date='2019-10-18', event_type='salida', time='12:10:30')
        events_mock = Mock(events=[event_mock_1, event_mock_2])
        self.events_detail.set(events_mock)
        events = self.events_detail.get()
        result = {'2019-10-18': [
            {'event_type': 'entrada', 'time': '07:10:21'},
            {'event_type': 'salida', 'time': '12:10:30'}]}
        self.assertEqual(events, result)
