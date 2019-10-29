import unittest

from src.t1000.domain.entity import Event, Events


class EventsTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_return_events(self):
        event_1 = Event('asdf', '2019-10-29', '13:00:30', 'salida')
        event_2 = Event('xcvb', '2019-10-21', '07:10:30', 'entrada')
        events = Events([event_1, event_2])
        self.assertListEqual(events.events, [event_1, event_2])
