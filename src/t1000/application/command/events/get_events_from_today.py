from .. import command_interface


class GetEventsFromToday(command_interface.CommandInterface):
    def execute(self):
        return self._repo.get_from_today()
