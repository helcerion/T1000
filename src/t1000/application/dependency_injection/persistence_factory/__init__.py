'''
from ....infrastructure import persistence as Persistence

def get() -> Persistence:
    return Persistence()
'''
from ....infrastructure.persistence import EventsInMemoryRepo

class EventsPersistenceFactory(object):
    @staticmethod
    def create(persitence_type):
        if persitence_type == 'in_memory':
            persistence = EventsInMemoryRepo()
        else:
            raise Exception('Persistence type %s does not supported' \
                % (persitence_type))

        return persistence
