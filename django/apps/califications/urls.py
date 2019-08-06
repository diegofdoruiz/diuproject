from django.urls import path
from .views import *
from apps.califications.views import *

app_name = 'califications'
urlpatterns = [
	path('', CalificationList.as_view(), name='calification'),
	path('create/', CalificationCreate.as_view(), name='create'),
	path('<int:pk>', CalificationDetail.as_view(), name='detail'),
	path('edit/<int:pk>', CalificationView.as_view(), name='edit'),
	path('delete/<int:pk>', CalificationDelete.as_view(), name='delete'),
]