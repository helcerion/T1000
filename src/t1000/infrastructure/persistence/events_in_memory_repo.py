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
        return self.__find(init=date, end=date)

    def get_from_interval(self, init: str = '', end: str = '') -> Events:
        init = None if init == '' else init
        end = None if end == '' else end

        return self.__find(init=init, end=end)
    
    def find_all(self):
        return self.__find(all=True)

    def save(self, event: Event):
        self._events.append(
            {'uuid': event.uuid, 'date': event.date, 'time': event.time}
        )

        return True

    def __find(self, init: str=None, end: str=None, all: bool=False):
        events = []
        event_type = ('entrada', 'salida')
        event_num = 0
        last_event = None

        for event in self._events:
            if self.__date_between_dates(init, end, event['date']) or \
                self.__date_before(init, end, event['date']) or \
                self.__date_after(init, end, event['date']) or all is True:
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
                last_event = self.__get_day(event['date'])
                events.append(event_entity)

        return Events(events)

    @classmethod
    def __date_between_dates(cls, init: str, end: str, date: str):
        date_between_dates = False
        
        if init is not None and end is not None and \
            cls.__get_date(date) >= cls.__get_date(init)\
            and cls.__get_date(date) <= cls.__get_date(end):
            date_between_dates = True

        return date_between_dates

    @classmethod
    def __date_before(cls, init: str, end: str, date: str):
        date_before = False

        if init is None and end is not None and \
            cls.__get_date(date) <= cls.__get_date(end):
            date_before = True
        
        return date_before

    @classmethod
    def __date_after(cls, init: str, end: str, date: str):
        date_after = False

        if init is not None and end is None and \
            cls.__get_date(date) >= cls.__get_date(init):
            date_after = True
        
        return date_after

    @classmethod
    def __get_date(cls, date: str):
        return datetime.strptime(date, cls.DATE_FORMAT).date()

    @classmethod
    def __get_day(cls, date: str):
        return datetime.strptime(date, cls.DATE_FORMAT).day
