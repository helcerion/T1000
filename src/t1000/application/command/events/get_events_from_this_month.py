from .. import command_abstract


class GetEventsFromThisMonth(command_abstract.CommandAbstract):
    def execute(self):
        return self._repo.get_month()
