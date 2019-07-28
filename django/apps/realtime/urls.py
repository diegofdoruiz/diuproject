from django.urls import path
from apps.realtime.views import CeleryRealTimeTemplateView

app_name = 'realtime'
urlpatterns = [
	path('', CeleryRealTimeTemplateView.as_view(), name='realtime'),
]