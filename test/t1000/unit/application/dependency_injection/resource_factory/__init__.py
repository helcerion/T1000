import unittest
from unittest.mock import patch

from src.t1000.application.dependency_injection.resource_factory import EventsResourceFactory


class EventsResourceFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    @patch('src.t1000.application.dependency_injection.resource_factory.EventsDetail')
    def test_create_with_exception(self, events_detail_mock):
        with self.assertRaises(Exception) as e:
            EventsResourceFactory.create('exception')

        self.assertEqual(str(e.exception), 'View exception does not supported')
        events_detail_mock.assert_not_called()

    @patch('src.t1000.application.dependency_injection.resource_factory.EventsDetail')
    def test_create(self, events_detail_mock):
        EventsResourceFactory.create('events_detail')
        events_detail_mock.assert_called_once()
