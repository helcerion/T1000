import unittest
from unittest.mock import patch, Mock
from datetime import datetime

from src.t1000.domain.repository import EventsRepo


class EventsRepoTestCase(unittest.TestCase):
    @patch('src.t1000.domain.repository.events_repo.datetime')
    def test_get_from_today(self, datetime_mock):
        datetime_mock.today.return_value = datetime(2019, 10, 1)
        persistence_mock = Mock()
        events_repo = EventsRepo(persistence=persistence_mock)
        events_repo.get_from_today()
        persistence_mock.get_from_date.assert_called_once_with('2019-10-01')

    def test_get_from_date(self):
        persistence_mock = Mock()
        events_repo = EventsRepo(persistence=persistence_mock)
        events_repo.get_from_date('2019-10-01')
        persistence_mock.get_from_date.assert_called_once_with('2019-10-01')

    @patch('src.t1000.domain.repository.events_repo.datetime')
    def test_get_month(self, datetime_mock):
        datetime_mock.today.return_value = datetime(2019, 9, 1)
        datetime_mock.strptime = datetime.strptime
        persistence_mock = Mock()
        events_repo = EventsRepo(persistence=persistence_mock)
        events_repo.get_month()
        persistence_mock.get_from_interval\
            .assert_called_once_with(init='2019-09-01', end='2019-09-30')
    
    def test_all(self):
        persistence_mock = Mock()
        events_repo = EventsRepo(persistence=persistence_mock)
        events_repo.all()
        persistence_mock.find_all.assert_called_once()

    def test_save(self):
        persistence_mock = Mock()
        event_mock = Mock()
        persistence_mock.save.return_value = True
        events_repo = EventsRepo(persistence=persistence_mock)
        saved = events_repo.save(event_mock)
        persistence_mock.save.assert_called_once_with(event_mock)
        self.assertTrue(saved)

    def test_save_with_error(self):
        persistence_mock = Mock()
        event_mock = Mock()
        persistence_mock.save.return_value = False
        events_repo = EventsRepo(persistence=persistence_mock)
        saved = events_repo.save(event_mock)
        persistence_mock.save.assert_called_once_with(event_mock)
        self.assertFalse(saved)
