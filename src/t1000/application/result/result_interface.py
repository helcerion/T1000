from ..command import command_interface
class ResultInterface(object):
    def __init__(self, command, resource):
        self._command: command_interface.CommandInterface = command
        self._resource = resource
    
    def get(self, *args, **kwargs):
        raise Exception(\
                'You need to implement get function form %s.' % \
                (self.__class__.__name__)\
            )
