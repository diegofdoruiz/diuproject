from django.urls import path
from apps.topics.views import TopicCreateView, TopicUpdateView, TopicListView, TopicDeleteView, TopicDetailView

app_name = 'topics'

urlpatterns = [
	path('', TopicListView.as_view(), name='topics'),
	path('create/', TopicCreateView.as_view(), name='create'),
	path('<int:pk>', TopicDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', TopicUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>',TopicDeleteView.as_view(), name='delete'),
]