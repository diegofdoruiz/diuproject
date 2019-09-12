"""diufirstprocjet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordChangeView, PasswordResetCompleteView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', TemplateView.as_view(template_name='home.html') , name='home'),
    path('realtime/', include('apps.realtime.urls', namespace='realtime')),
    path('arduino/', include('apps.arduino.urls', namespace='arduino')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('roles/', include('apps.roles.urls', namespace='roles')),
    path('questions/', include('apps.questions.urls', namespace='questions')),
    path('', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    path('topics/', include('apps.topics.urls', namespace='topics')),
    path('courses/', include('apps.courses.urls', namespace='courses')),
    path('games/', include('apps.games.urls', namespace='games')),
    path('califications/', include('apps.califications.urls', namespace='califications')),
]
