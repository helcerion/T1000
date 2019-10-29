import unittest

from src.t1000.application.dependency_injection.resource_factory import EventsResourceFactory, EventsDetail


class EventsResourceFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_create_with_exception(self):
        with self.assertRaises(Exception) as e:
            EventsResourceFactory.create('exception')

        self.assertEqual(str(e.exception), 'View exception does not supported')

    def test_create(self):
        resource = EventsResourceFactory.create('events_detail')
        self.assertEqual(type(resource), EventsDetail)