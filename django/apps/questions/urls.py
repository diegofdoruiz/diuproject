from django.urls import path
from .views import *
from apps.questions.views import *

app_name = 'questions'
urlpatterns = [
	path('', QuestionList.as_view(), name='question'),
	path('listAnswer', AnswerList.as_view(), name='listAnswer'),
	path('create/', QuestionCreate.as_view(), name='create'),
	path('createAnswer/', AnswerCreate.as_view(), name='createAnswer'),
	path('<int:pk>', QuestionDetail.as_view(), name='detail'),
	path('detailAnswer/<int:pk>', AnswerDetail.as_view(), name='detailAnswer'),
	path('edit/<int:pk>', QuestionView.as_view(), name='edit'),
	path('editAnswer/<int:pk>', AnswerView.as_view(), name='editAnswer'),
	path('delete/<int:pk>', QuestionDelete.as_view(), name='delete'),
]