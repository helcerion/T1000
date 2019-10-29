import unittest

from src.t1000.application.command.events import GetEventsFromThisMonth
from src.t1000.domain.entity import Event, Events
from src.t1000.domain.repository import EventsRepo
from src.t1000.infrastructure.persistence import EventsInMemoryRepo


class GetEventsFromThisMonthTestCase(unittest.TestCase):
    _repo: EventsRepo
    _events: Events

    @classmethod
    def setUpClass(cls):
        super(GetEventsFromThisMonthTestCase, cls).setUpClass()
        cls._repo = EventsRepo(EventsInMemoryRepo())
        cls._events = Events([Event('asdf', '2019-10-01', '07:20:00', 'entrada'),
                              Event('qwer', '2019-10-01', '14:35:00', 'salida'),
                              Event('zxcv', '2019-10-15', '07:05:30', 'entrada'),
                              Event('zxcv', '2019-10-15', '08:05:30', 'salida'),
                              Event('zxcv', '2019-10-15', '09:05:30', 'entrada'),
                              Event('zxcv', '2019-10-15', '09:15:30', 'salida'),
                              Event('zxcv', '2019-10-15', '10:05:30', 'entrada'),
                              Event('zxcv', '2019-10-16', '07:05:30', 'entrada'),
        ])

    def setUp(self):
        super(GetEventsFromThisMonthTestCase, self).setUp()
        self._command = GetEventsFromThisMonth(self._repo)

    def tearDown(self):
        self._command = None
        return super(GetEventsFromThisMonthTestCase, self).tearDown()
    
    @classmethod
    def tearDownClass(cls):
        cls._repo = None
        cls._events = None
        return super(GetEventsFromThisMonthTestCase, cls).tearDownClass()

    def test_execute(self):
        self.assertEqual(self._command.execute(), self._events)

    def test_set_params_return_self(self):
        command_result = self._command.set_params()
        self.assertEqual(command_result, self._command)
