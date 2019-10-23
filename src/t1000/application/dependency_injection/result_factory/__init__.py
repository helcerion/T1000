'''
from ....application import result as Result
from .. import command_factory as CommandFactory
from .. import persistence_factory as PersistenceFactory
from .. import repository_factory as RepositoryFactory
from .. import resource_factory as ResourceFactory

def get() -> Result:
    persitence = PersistenceFactory.get()
    repository = RepositoryFactory.get(persitence)
    command = CommandFactory.get(repository)
    resource = ResourceFactory.get()

    return Result(command, resource)
'''
from ..resource_factory import EventsResourceFactory
from ..command_factory import EventsCommandFactory
from ...result.events import ConsoleEventsResult, HtmlEventsResult


class EventsResultFactory():
    @staticmethod
    def create(result_type, resource_type, use_case, entity, persistence_type,
               *args, **kwargs):
        '''
            result_type='cmd'
            resource_type='events_detail'
            use_case='get_events_from_today'
            entity='Events'
            persistence_type='in_memory'
        '''
        resource = EventsResourceFactory.create(resource_type)
        command = EventsCommandFactory.create(
                use_case=use_case,
                entity=entity,
                persistence_type=persistence_type
            )

        if result_type == 'cmd':
            result = ConsoleEventsResult(command, resource)
        elif result_type == 'html':
            result = HtmlEventsResult(command, resource)
        else:
            raise Exception('Result type %s does not supported' %
                            (result_type))

        return result
