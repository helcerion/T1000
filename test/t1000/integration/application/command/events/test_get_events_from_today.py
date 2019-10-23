import unittest

from src.t1000.application.command.events import GetEventsFromToday
from src.t1000.domain.repository import EventsRepo
from src.t1000.domain.entity import Events
from src.t1000.infrastructure.persistence import EventsInMemoryRepo


class GetEventsFromTodayTestCase(unittest.TestCase):
    _repo: EventsRepo
    _command: GetEventsFromToday

    @classmethod
    def setUpClass(cls):
        super(GetEventsFromTodayTestCase, cls).setUpClass()
        cls._repo = EventsRepo(EventsInMemoryRepo())

    def setUp(self):
        super(GetEventsFromTodayTestCase, self).setUp()
        self._command = GetEventsFromToday(self._repo)

    def tearDown(self):
        return super(GetEventsFromTodayTestCase, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        return super(GetEventsFromTodayTestCase, cls).tearDownClass()

    def test_execute(self):
        self.assertEqual(self._command.execute(), Events([]))
