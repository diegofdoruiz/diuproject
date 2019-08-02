from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.topics.models import Topic
from apps.topics.forms import TopicForm
from django.urls import reverse_lazy

# Create your views here.


class TopicListView(ListView):
    model = Topic
    template_name = 'topics.html'

class TopicDetailView(DetailView):
    model = Topic
    template_name= 'topic_detail.html'

class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'topic_form.html'
    success_url= reverse_lazy('topics:topics')


class TopicUpdateView(UpdateView):
    model = Topic
    form_class = TopicForm
    success_url= reverse_lazy('topics:topics')
    template_name = 'topic_form.html'
    
class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy('topics:topics')
   




