from .. import command_interface

class GetEventsFromThisMonth(command_interface.CommandInterface):
    def execute(self):
        return self._repo.getMonth()
