from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.courses.models import Course
from apps.courses.forms import CourseForm
from django.urls import reverse_lazy
from apps.users.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

@method_decorator(login_required, name='dispatch')
class CourseListView(PermissionRequiredMixin, ListView):
    model = Course
    permission_required = 'courses.view_course'
    template_name = 'courses.html'

@method_decorator(login_required, name='dispatch')
class CourseDetailView(PermissionRequiredMixin, DetailView):
    model = Course
    permission_required = 'courses.view_course'
    template_name = 'course_detail.html'

@method_decorator(login_required, name='dispatch')
class CourseCreateView(PermissionRequiredMixin, CreateView):
    model = Course
    permission_required = 'courses.add_course'
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('courses:courses')

@method_decorator(login_required, name='dispatch')
class CourseUpdateView(PermissionRequiredMixin, UpdateView):
    model = Course
    permission_required = 'courses.change_course'
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('courses:courses')

@method_decorator(login_required, name='dispatch')
class CourseDeleteView(PermissionRequiredMixin, DeleteView):
    model = Course
    permission_required = 'courses.delete_course'
    success_url = reverse_lazy('courses:courses')
