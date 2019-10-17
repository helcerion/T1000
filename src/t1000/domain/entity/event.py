class Event(object):
    def __init__(self, uuid: str, date: str, time: str, event_type: str):
        self._uuid = uuid
        self._date = date
        self._time = time
        self._event_type = event_type
    
    def __str__(self):
        return ' '.join([str(self.uuid), str(self.date), str(self.time), \
            str(self.event_type)])

    @property
    def uuid(self) -> str:
        return self._uuid

    @property
    def date(self) -> str:
        return self._date

    @property
    def time(self) -> str:
        return self._time
    
    @property
    def event_type(self) -> str:
        return self._event_type
