import unittest
from unittest.mock import patch, Mock
from datetime import datetime

from src.t1000.infrastructure.persistence import EventsInMemoryRepo


class EventsInMemoryRepoTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Event')
    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Events')
    def test_get_from_date_one_event(self, events_mock, event_mock):
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.get_from_date('2019-10-16')
        event_mock.assert_called_once()
        args, kwargs = events_mock.call_args
        self.assertEqual(len(args[0]), 1)

    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Event')
    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Events')
    def test_get_from_date_more_events(self, events_mock, event_mock: Mock):
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.get_from_date('2019-10-15')
        self.assertEqual(event_mock.call_count, 5)
        args, kwargs = events_mock.call_args
        self.assertEqual(len(args[0]), 5)

    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Event')
    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Events')
    def test_get_from_interval(self, events_mock, event_mock):
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.get_from_interval('2019-10-15', '2019-10-16')
        self.assertEqual(event_mock.call_count, 6)
        args, kwargs = events_mock.call_args
        self.assertEqual(len(args[0]), 6)

    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Event')
    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Events')
    def test_find_all(self, events_mock, event_mock):
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.find_all()
        self.assertEqual(event_mock.call_count, 8)
        args, kwargs = events_mock.call_args
        self.assertEqual(len(args[0]), 8)

    def test_save(self):
        event_to_save = Mock(date=datetime.today().date().isoformat())
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.save(event_to_save)
        events_result = events_in_memory_repo.find_all()
        self.assertEqual(len(events_result.events), 9)
        events_result = events_in_memory_repo.get_from_date(datetime.today()\
                                                            .date().isoformat())
        self.assertEqual(len(events_result.events), 1)

    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Event')
    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Events')
    def test_events_before_date(self, events_mock, event_mock):
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.get_from_interval(end='2019-10-10')
        self.assertEqual(event_mock.call_count, 2)
        args, kwargs = events_mock.call_args
        self.assertEqual(len(args[0]), 2)


    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Event')
    @patch('src.t1000.infrastructure.persistence.events_in_memory_repo.Events')
    def test_events_after_date(self, events_mock, event_mock):
        events_in_memory_repo = EventsInMemoryRepo()
        events_in_memory_repo.get_from_interval(init='2019-10-02')
        self.assertEqual(event_mock.call_count, 6)
        args, kwargs = events_mock.call_args
        self.assertEqual(len(args[0]), 6)
