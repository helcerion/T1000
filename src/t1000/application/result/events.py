from . import result_interface


class ConsoleEventsResult(result_interface.ResultInterface):
    def get(self, *args, **kwargs):
        try:
            events = self._command.set_params(*args, **kwargs).execute()
            self._resource.set(events)

            body = self._resource.get()
            code = 0
        except Exception:
            body = {}
            code = 1

        return body, code


class HtmlEventsResult(result_interface.ResultInterface):
    def get(self, *args, **kwargs):
        try:
            events = self._command.set_params(*args, **kwargs).execute()
            self._resource.set(events)

            body = {'events': self._resource.get()}
            status = 200
        except Exception:
            body = {}
            status = 500

        return body, status
