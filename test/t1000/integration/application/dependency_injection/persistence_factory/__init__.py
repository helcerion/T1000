import unittest

from src.t1000.application.dependency_injection.persistence_factory import EventsPersistenceFactory
from src.t1000.infrastructure.persistence import EventsInMemoryRepo


class EventsPersistenceFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_create_with_exception(self):
        with self.assertRaises(Exception) as e:
            EventsPersistenceFactory.create('exception')

        self.assertEqual(str(e.exception), 'Persistence type exception does not supported')

    def test_create(self):
        persistence = EventsPersistenceFactory.create('in_memory')
        self.assertEqual(type(persistence), EventsInMemoryRepo)
