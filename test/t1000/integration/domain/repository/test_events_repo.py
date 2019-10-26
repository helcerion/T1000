import unittest

from datetime import datetime

from src.t1000.domain.repository import EventsRepo
from src.t1000.infrastructure.persistence import EventsInMemoryRepo
from src.t1000.domain.entity import Event, Events


class EventsRepoTestCase(unittest.TestCase):
    def test_get_from_today_with_in_memory_repo(self):
        event = Event('asdf', datetime.today().date().isoformat(), datetime.today().time().isoformat('seconds'), 'entrada')
        event_in_memory_repo = EventsInMemoryRepo()
        event_in_memory_repo.create(event)
        events_repo = EventsRepo(EventsInMemoryRepo())
        events = events_repo.get_from_today()
        self.assertEqual(str(events), '')
    
    def test_get_from_date_with_in_memory_repo(self):
        events_repo = EventsRepo(EventsInMemoryRepo())
        events = events_repo.get_from_date('2019-10-16')
        self.assertEqual(str(events), 'zxcv 2019-10-16 07:05:30 entrada')

    def test_get_from_month_with_in_memory_repo(self):
        events_repo = EventsRepo(EventsInMemoryRepo())
        events = events_repo.get_month()
        self.assertEqual(str(events), 'asdf 2019-10-01 07:20:00 entrada\nqwer 2019-10-01 14:35:00 salida\nzxcv 2019-10-15 07:05:30 entrada\nzxcv 2019-10-15 08:05:30 salida\nzxcv 2019-10-15 09:05:30 entrada\nzxcv 2019-10-15 09:15:30 salida\nzxcv 2019-10-15 10:05:30 entrada\nzxcv 2019-10-16 07:05:30 entrada')

    def test_all_from_month_with_in_memory_repo(self):
        events_repo = EventsRepo(EventsInMemoryRepo())
        events = events_repo.all()
        self.assertEqual(str(events), 'asdf 2019-10-01 07:20:00 entrada\nqwer 2019-10-01 14:35:00 salida\nzxcv 2019-10-15 07:05:30 entrada\nzxcv 2019-10-15 08:05:30 salida\nzxcv 2019-10-15 09:05:30 entrada\nzxcv 2019-10-15 09:15:30 salida\nzxcv 2019-10-15 10:05:30 entrada\nzxcv 2019-10-16 07:05:30 entrada')
