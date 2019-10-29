from ..command import command_abstract


class ResultAbstract():
    _command: command_abstract.CommandAbstract

    def __init__(self, command: command_abstract.CommandAbstract, resource):
        self._command = command
        self._resource = resource

    def set_command(self, command: command_abstract.CommandAbstract):
        self._command = command

    def set_resource(self, resource):
        self._resource = resource

    def get(self, *args, **kwargs):
        raise Exception(
                'You need to implement get function from %s.' %
                (self.__class__.__name__)
            )
