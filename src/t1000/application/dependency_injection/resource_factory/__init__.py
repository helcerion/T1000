'''
from ....application import resource as Resource

def get() -> Resource:
    return Resource()
'''
from ...resource.events import EventsDetail


class EventsResourceFactory():
    @staticmethod
    def create(view):
        if view == 'events_detail':
            resource = EventsDetail
        else:
            raise Exception('View %s does not supported' % (view))

        return resource
