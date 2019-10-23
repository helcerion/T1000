class CommandInterface():
    def __init__(self, repository):
        self._repo = repository

    def set_params(self, *args, **kwargs):
        return self

    def execute(self):
        raise Exception(
                'You need to implement execute function from %s.' %
                (self.__class__.__name__)
            )
