import unittest

from src.t1000.application.dependency_injection.repository_factory import EventsRepositoryFactory
from src.t1000.domain.repository import EventsRepo


class EventRepositoryFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_with_persistence_exception(self):
        with self.assertRaises(Exception) as e:
            EventsRepositoryFactory.create('exception', 'exception')

        self.assertEqual(str(e.exception), 'Persistence type exception does not supported')

    def test_create_with_exception(self):
        with self.assertRaises(Exception) as e:
            EventsRepositoryFactory.create('exception', 'in_memory')

        self.assertEqual(str(e.exception), 'Repository from exception does not supported')

    def test_create(self):
        repo = EventsRepositoryFactory.create('Events', 'in_memory')
        self.assertEqual(type(repo), EventsRepo)
    