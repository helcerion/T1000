import unittest

from src.t1000.application.dependency_injection.command_factory import EventsCommandFactory
from src.t1000.application.command.events import GetEventsFromToday, GetEventsFromThisMonth


class EventsCommandFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_with_exception_persistence(self):
        with self.assertRaises(Exception) as e:
            EventsCommandFactory.create('exception', 'exception', 'exception')

        self.assertEqual(str(e.exception), 'Persistence type exception does not supported')

    def test_create_with_exception_repository(self):
        with self.assertRaises(Exception) as e:
            EventsCommandFactory.create('exception', 'exception', 'in_memory')

        self.assertEqual(str(e.exception), 'Repository from exception does not supported')

    def test_create_with_exception(self):
        with self.assertRaises(Exception) as e:
            EventsCommandFactory.create('exception', 'Events', 'in_memory')

        self.assertEqual(str(e.exception), 'Command exception does not supported')

    def test_create_today(self):
        command = EventsCommandFactory.create('get_events_from_today', 'Events', 'in_memory')
        self.assertEqual(type(command), GetEventsFromToday)

    def test_create_this_month(self):
        command = EventsCommandFactory.create('get_events_this_month', 'Events', 'in_memory')
