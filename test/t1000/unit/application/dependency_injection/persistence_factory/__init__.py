import unittest
from unittest.mock import patch

from src.t1000.application.dependency_injection.persistence_factory import EventsPersistenceFactory

class EventsPersistenceFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_with_exception(self):
        with self.assertRaises(Exception) as e:
            EventsPersistenceFactory.create('exception')

        self.assertEqual(str(e.exception), 'Persistence type exception does not supported')
    
    @patch('src.t1000.application.dependency_injection.persistence_factory.EventsInMemoryRepo')
    def test_create(self, in_memory_mock):
        persistence = EventsPersistenceFactory.create('in_memory')
        in_memory_mock.assert_called_once()
