import unittest

from src.t1000.domain.entity import Event

class EventTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_equal_events(self):
        event_entity_1 = Event('asdf', '2019-10-19', '07:05:00', 'entrada')
        event_entity_2 = Event('asdf', '2019-10-19', '07:05:00', 'entrada')
        self.assertEqual(event_entity_1, event_entity_2)

    def test_not_equal_events(self):
        event_entity_1 = Event('asdf', '2019-10-19', '07:05:00', 'entrada')
        event_entity_2 = Event('asdu', '2019-10-19', '07:05:00', 'entrada')
        self.assertNotEqual(event_entity_1, event_entity_2)
