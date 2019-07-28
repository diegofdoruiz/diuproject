from django.urls import path
from .views import *

app_name = 'arduino'
urlpatterns = [
	path('', home, name='home'),
	path('test/', test, name='test'),
]