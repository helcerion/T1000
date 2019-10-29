import unittest

from src.t1000.application.dependency_injection.result_factory import EventsResultFactory, ConsoleEventsResult, HtmlEventsResult


class EventsResultFactoryTestCase(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_create_with_view_exception(self):
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'exception', 'exception', 'exception', 'exception')
        
        self.assertEqual(str(e.exception), 'View exception does not supported')

    def test_create_with_persistence_exception(self):
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'events_detail', 'exception', 'exception', 'exception')
        
        self.assertEqual(str(e.exception), 'Persistence type exception does not supported')

    def test_create_with_respository_exception(self):
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'events_detail', 'exception', 'exception', 'in_memory')
        
        self.assertEqual(str(e.exception), 'Repository from exception does not supported')

    def test_create_with_command_exception(self):
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'events_detail', 'exception', 'Events', 'in_memory')
        
        self.assertEqual(str(e.exception), 'Command exception does not supported')

    def test_create_with_exception(self):
        with self.assertRaises(Exception) as e:
            EventsResultFactory.create('exception', 'events_detail', 'get_events_from_today', 'Events', 'in_memory')
        
        self.assertEqual(str(e.exception), 'Result type exception does not supported')

    def test_create_cmd(self):
        cmd = EventsResultFactory.create('cmd', 'events_detail', 'get_events_from_today', 'Events', 'in_memory')
        self.assertEqual(type(cmd), ConsoleEventsResult)

    def test_create_html(self):
        html = EventsResultFactory.create('html', 'events_detail', 'get_events_from_today', 'Events', 'in_memory')
        self.assertEqual(type(html), HtmlEventsResult)
