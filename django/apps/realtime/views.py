from django.http import HttpResponse
from django.views.generic import TemplateView

from .tasks import listenArduino

class CeleryRealTimeTemplateView(TemplateView):
    template_name = 'realtime.html'

    def post(self, request, *args, **kwargs):
        task_id = listenArduino.delay()
        return HttpResponse(task_id)


