import unittest
from unittest.mock import patch, Mock

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

    def test_find_all(self):
        self.assertTrue(False)

    def test_create(self):
        self.aassertTrue(False)
