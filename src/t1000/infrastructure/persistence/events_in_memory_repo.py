from datetime import datetime

from ...domain.entity import Events, Event

class EventsInMemoryRepo(object):
    DATE_FORMAT = '%Y-%m-%d'

    def __init__(self):
        self._events = [
            {'uuid': 'asdf', 'date': '2019-10-01', 'time': '07:20:00'},
            {'uuid': 'qwer', 'date': '2019-10-01', 'time': '14:35:00'},
            {'uuid': 'zxcv', 'date': '2019-10-15', 'time': '07:05:30'},
            {'uuid': 'zxcv', 'date': '2019-10-15', 'time': '08:05:30'},
            {'uuid': 'zxcv', 'date': '2019-10-15', 'time': '09:05:30'},
            {'uuid': 'zxcv', 'date': '2019-10-15', 'time': '09:15:30'},
            {'uuid': 'zxcv', 'date': '2019-10-15', 'time': '10:05:30'},
            {'uuid': 'zxcv', 'date': '2019-10-16', 'time': '07:05:30'},
        ]

    def getFromDate(self, date: str) -> Events:
        events = []
        event_type = ('entrada', 'salida')
        event_num = 0
        last_event = None

        for e in self._events:
            if self.__get_date(e['date']) == self.__get_date(date):
                if last_event is None or last_event != self.__get_day(e['date']):
                    event_num = 0

                event = Event(uuid=e['uuid'], date=e['date'], time=e['time'], \
                    event_type=event_type[event_num%2])
                event_num += 1
                last_event = self.__get_day(event.date)
                events.append(event)

        return Events(events) 

    def getFromInterval(self, init: str, end: str) -> Events:
        events = []
        event_type = ('entrada', 'salida')
        event_num = 0
        last_event = None

        for e in self._events:
            if self.__get_date(e['date']) >= self.__get_date(init) or self.__get_date(e['date']) <= self.__get_date(end):
                if last_event is None or last_event != self.__get_day(e['date']):
                    event_num = 0

                event = Event(uuid=e['uuid'], date=e['date'], time=e['time'], \
                    event_type=event_type[event_num%2])
                event_num += 1
                last_event = self.__get_day(event.date)
                events.append(event)

        return Events(events) 

    @classmethod
    def __get_date(cls, date: str):
        return datetime.strptime(date, cls.DATE_FORMAT).date()

    @classmethod
    def __get_day(cls, date: str):
        return datetime.strptime(date, cls.DATE_FORMAT).day
