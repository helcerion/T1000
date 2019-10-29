import unittest
from unittest.mock import patch

from src.t1000.application.dependency_injection.repository_factory import EventsRepositoryFactory


class EventRepositoryFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_with_persistence_exception(self):
        with self.assertRaises(Exception) as e:
            EventsRepositoryFactory.create('exception', 'exception')

        self.assertEqual(str(e.exception), 'Persistence type exception does not supported')

    @patch('src.t1000.application.dependency_injection.repository_factory.EventsPersistenceFactory')
    def test_create_with_exception(self, persistence_factory_mock):
        with self.assertRaises(Exception) as e:
            EventsRepositoryFactory.create('exception', 'in_memory')

        persistence_factory_mock.create.assert_called_once_with(persistence_type='in_memory')
        self.assertEqual(str(e.exception), 'Repository from exception does not supported')

    @patch('src.t1000.application.dependency_injection.repository_factory.EventsRepo')
    @patch('src.t1000.application.dependency_injection.repository_factory.EventsPersistenceFactory')
    def test_create(self, persistence_factory_mock, repo_mock):
        EventsRepositoryFactory.create('Events', 'in_memory')
        persistence_factory_mock.create.assert_called_once_with(persistence_type='in_memory')
        repo_mock.assert_called_once()
    