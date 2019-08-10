from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
	path('', CourseListView.as_view(), name='courses'),
	path('create/', CourseCreateView.as_view(), name='create'),
	path('<int:pk>', CourseDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', CourseUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>', CourseDeleteView.as_view(), name='delete')
]