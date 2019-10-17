from ....domain.entity import Events

class EventsDetail(object):
    @staticmethod
    def get(events: Events):
        events_resource = dict()

        for event in events.events:
            if event.date not in events_resource.keys():
                events_resource[event.date] = list()

            event_resource = dict()
            event_resource['event_type'] = event.event_type
            event_resource['time'] = event.time
            events_resource[event.date].append(event_resource)
        
        return events_resource
