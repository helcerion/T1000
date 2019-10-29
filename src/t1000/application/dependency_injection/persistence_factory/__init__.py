'''
from ....infrastructure import persistence as Persistence

def get() -> Persistence:
    return Persistence()
'''
from ....infrastructure.persistence import EventsInMemoryRepo


class EventsPersistenceFactory():
    @staticmethod
    def create(persistence_type):
        if persistence_type == 'in_memory':
            persistence = EventsInMemoryRepo()
        else:
            raise Exception('Persistence type %s does not supported' %
                            (persistence_type))

        return persistence
