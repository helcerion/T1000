from django.urls import re_path

from src.t1000.application.dependency_injection.result_factory import EventsResultFactory
from .views import EventsView

app_name = 't1000'
urlpatterns = [
    re_path(r'^events/this/month/$', EventsView.as_view(\
        result_factory=EventsResultFactory, \
        result_type='html', \
        resource_type='events_detail', \
        use_case='get_events_this_month', \
        entity='Events', \
        persistence_type='in_memory', \
        template_name='t1000/list_events.html'\
    ), name='events_this_month'),
]
