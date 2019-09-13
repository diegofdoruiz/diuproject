from django.urls import path
from .views import *
from apps.users.views import UserListView, UserDeleteView, UserDetailView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordChangeView, PasswordResetCompleteView

app_name = 'users'
urlpatterns = [
	path('', UserListView.as_view(), name='users'),
	path('create/', create, name='create'),
	path('<int:pk>', UserDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', edit, name='edit'),
	path('delete/<int:pk>', UserDeleteView.as_view(), name='delete'),
	path('home/', home, name='home')
	# path('login/', LoginView.as_view(template_name='login.html'), name="login"),
]