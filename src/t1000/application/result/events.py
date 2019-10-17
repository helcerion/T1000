from . import result_interface

class ConsoleEventsResult(result_interface.ResultInterface):
    def get(self, *args, **kwargs):
        events = self._command.set_params(*args, **kwargs).execute()

        body = self._resource.get(events)

        return body

class HtmlEventsResult(result_interface.ResultInterface):
    def get(self, *args, **kwargs):
        events = self._command.set_params(*args, **kwargs).execute()

        body = {'events': self._resource.get(events)}
        status = 200

        return body, status
