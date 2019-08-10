from django.urls import path
from .views import *
from apps.questions.views import *

app_name = 'questions'
urlpatterns = [
	path('', QuestionList.as_view(), name='question'),
	path('create/', QuestionCreate.as_view(), name='create'),
	path('<int:pk>', QuestionDetail.as_view(), name='detail'),
	path('edit/<int:pk>', QuestionView.as_view(), name='edit'),
	path('delete/<int:pk>', QuestionDelete.as_view(), name='delete'),
]