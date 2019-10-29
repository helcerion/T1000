import unittest

from datetime import datetime

from src.t1000.infrastructure.persistence import EventsInMemoryRepo
from src.t1000.domain.entity import Event, Events


class EventsInMemoryRepoTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_get_from_date_one_event(self):
        event = Event('zxcv', '2019-10-16', '07:05:30', 'entrada')
        events = Events([event])
        events_in_memory_repo = EventsInMemoryRepo()
        events_result = events_in_memory_repo.get_from_date('2019-10-16')
        self.assertEqual(events_result, events)

    def test_get_from_date_more_events(self):
        events_in_memory_repo = EventsInMemoryRepo()
        events_result = events_in_memory_repo.get_from_date('2019-10-15')
        self.assertEqual(len(events_result.events), 5)

    def test_get_from_interval(self):
        events_in_memory_repo = EventsInMemoryRepo()
        events_result = events_in_memory_repo.get_from_interval(
            '2019-10-15', '2019-10-16')
        self.assertEqual(len(events_result.events), 6)

    def test_find_all(self):
        events_in_memory_repo = EventsInMemoryRepo()
        events_result = events_in_memory_repo.find_all()
        self.assertEqual(len(events_result.events), 8)

    def test_save(self):
        event_to_save = Event(uuid='asdf', \
            date=datetime.today().date().isoformat(), \
            time=datetime.today().time().isoformat('seconds'), \
            event_type='entrada')
        events_in_memory_repo = EventsInMemoryRepo()
        saved = events_in_memory_repo.save(event_to_save)
        self.assertTrue(saved)
        events_results = events_in_memory_repo.find_all()
        self.assertEqual(len(events_results.events), 9)
        events = events_in_memory_repo.get_from_date(datetime.today().date()\
                                                     .isoformat())
        self.assertEqual(len(events.events), 1)
        event = events.events[0]
        self.assertEqual(event, event_to_save)

    def test_events_before_date(self):
        events_in_memory_repo = EventsInMemoryRepo()
        events_result = events_in_memory_repo.get_from_interval(end='2019-10-10')
        self.assertEqual(len(events_result.events), 2)

    def test_events_after_date(self):
        events_in_memory_repo = EventsInMemoryRepo()
        events_result = events_in_memory_repo.get_from_interval(init='2019-10-02')
        self.assertEqual(len(events_result.events), 6)
