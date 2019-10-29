from . import result_abstract


class ConsoleEventsResult(result_abstract.ResultAbstract):
    def get(self, *args, **kwargs):
        try:
            if self._command is None:
                raise Exception('Result needs a command.')
            if self._resource is None:
                raise Exception('Result needs resource.')

            events = self._command.set_params(*args, **kwargs).execute()
            self._resource.set(events)

            body = self._resource.get()
            code = 0
        except Exception as e:
            body = {'message': str(e)}
            code = 1

        return body, code


class HtmlEventsResult(result_abstract.ResultAbstract):
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
