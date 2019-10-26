import unittest
from unittest.mock import MagicMock, Mock

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

    def test_str(self):
        event_mock_1 = MagicMock()
        event_mock_2 = MagicMock()
        event_mock_1.__str__.return_value = 'asdf 2019-10-21 07:05:00 entrada' 
        event_mock_2.__str__.return_value = 'qwer 2019-10-21 14:05:00 salida'
        events_entity = Events([event_mock_1, event_mock_2])
        self.assertEqual(str(events_entity), 'asdf 2019-10-21 07:05:00 entrada\nqwer 2019-10-21 14:05:00 salida')
