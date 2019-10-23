import unittest
from unittest.mock import Mock

from src.t1000.domain.entity import Events


class EventsTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_equal_events(self):
        event_mock_1 = Mock()
        events_entity_1 = Events([event_mock_1])
        events_entity_2 = Events([event_mock_1])
        self.assertEqual(events_entity_1, events_entity_2)
    
    def test_not_equal_events(self):
        event_mock_1 = Mock()
        event_mock_2 = Mock()
        events_entity_1 = Events([event_mock_1])
        events_entity_2 = Events([event_mock_2])
        self.assertNotEqual(events_entity_1, events_entity_2)
        