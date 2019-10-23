from typing import List
from . import Event


class Events():
    def __init__(self, events: List[Event]):
        self._events = events

    def __str__(self):
        return '\n'.join([str(event) for event in self.events])

    def __eq__(self, value):
        return self.events == value.events

    @property
    def events(self) -> List[Event]:
        return self._events
