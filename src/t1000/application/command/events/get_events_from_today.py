from .. import command_abstract


class GetEventsFromToday(command_abstract.CommandAbstract):
    def execute(self):
        return self._repo.get_from_today()
