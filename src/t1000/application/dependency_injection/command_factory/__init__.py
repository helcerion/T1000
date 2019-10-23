'''
from ....application import command as Command
from ....domain import repository as Repository

def get(repository: Repository) -> Command:
    return Command(repository)
'''
from ..repository_factory import EventsRepositoryFactory
from ...command.events import GetEventsFromToday, GetEventsFromThisMonth


class EventsCommandFactory():
    @staticmethod
    def create(use_case, entity, persistence_type):
        repository = EventsRepositoryFactory.create(entity, persistence_type)

        if use_case == 'get_events_from_today':
            command = GetEventsFromToday(repository)
        elif use_case == 'get_events_this_month':
            command = GetEventsFromThisMonth(repository)
        else:
            raise Exception('Command %s does not supported' % (use_case))

        return command
