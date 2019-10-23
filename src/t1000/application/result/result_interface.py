from ..command import command_interface


class ResultInterface():
    _command: command_interface.CommandInterface

    def __init__(self, command: command_interface, resource):
        self._command = command
        self._resource = resource

    def set_command(self, command: command_interface.CommandInterface):
        self._command = command

    def set_reource(self, resource):
        self._resource = resource

    def get(self, *args, **kwargs):
        raise Exception(
                'You need to implement get function from %s.' %
                (self.__class__.__name__)
            )
