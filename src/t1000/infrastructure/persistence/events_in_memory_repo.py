from datetime import datetime

from ...domain.entity import Event, Events


class EventsInMemoryRepo():
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

    def get_from_date(self, date: str) -> Events:
        events = []
        event_type = ('entrada', 'salida')
        event_num = 0
        last_event = None

        for event in self._events:
            if self.__get_date(event['date']) == self.__get_date(date):
                if last_event is None or \
                   last_event != self.__get_day(event['date']):
                    event_num = 0

                event_entity = Event(
                        uuid=event['uuid'],
                        date=event['date'],
                        time=event['time'],
                        event_type=event_type[event_num % 2]
                    )
                event_num += 1
                last_event = self.__get_day(event_entity.date)
                events.append(event_entity)

        return Events(events)

    def get_from_interval(self, init: str, end: str) -> Events:
        events = []
        event_type = ('entrada', 'salida')
        event_num = 0
        last_event = None

        for event in self._events:
            if self.__get_date(event['date']) >= self.__get_date(init) or \
               self.__get_date(event['date']) <= self.__get_date(end):
                if last_event is None or \
                   last_event != self.__get_day(event['date']):
                    event_num = 0

                event_entity = Event(
                        uuid=event['uuid'],
                        date=event['date'],
                        time=event['time'],
                        event_type=event_type[event_num % 2]
                    )
                event_num += 1
                last_event = self.__get_day(event_entity.date)
                events.append(event_entity)

        return Events(events)

    @classmethod
    def __get_date(cls, date: str):
        return datetime.strptime(date, cls.DATE_FORMAT).date()

    @classmethod
    def __get_day(cls, date: str):
        return datetime.strptime(date, cls.DATE_FORMAT).day
