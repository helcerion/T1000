'''
from ....domain import repository as Repository
from ....infrastructure import persistence as Persistence

def get(persistence: Persistence) -> Repository:
    return Repository(persistence)
'''
from ..persistence_factory import EventsPersistenceFactory
from ....domain.repository import EventsRepo


class EventsRepositoryFactory():
    @staticmethod
    def create(entity, persistence_type):
        persistence = EventsPersistenceFactory.create(
                persistence_type=persistence_type
            )

        if entity == 'Events':
            repository = EventsRepo(persistence=persistence)
        else:
            raise Exception('Repository from %s does not supported' % (entity))

        return repository
