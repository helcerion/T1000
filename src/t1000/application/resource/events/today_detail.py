from ....domain.entity import Events


class EventsDetail():
    def __init__(self):
        self._events_resource = dict()

    def set(self, events: Events):
        for event in events.events:
            if event.date not in self._events_resource.keys():
                self._events_resource[event.date] = list()

            event_resource = dict()
            event_resource['event_type'] = event.event_type
            event_resource['time'] = event.time
            self._events_resource[event.date].append(event_resource)

    def get(self):
        return self._events_resource
