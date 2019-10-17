from django.shortcuts import render
from django.views import View

# Create your views here.
class EventsView(View):
    result_factory = None
    result_type = None
    resource_type = None
    use_case = None
    entity = None
    persistence_type = None
    template_name = None

    def get(self, request, *args, **kwargs):
        body, status = self.result_factory.create(\
                result_type=self.result_type, \
                resource_type=self.resource_type, \
                use_case=self.use_case, \
                entity=self.entity, \
                persistence_type=self.persistence_type, \
                **kwargs\
            ).get(*args, **kwargs)

        return render(request, self.template_name, body, status=status)
