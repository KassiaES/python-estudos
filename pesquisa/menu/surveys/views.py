from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView
from .models import Question

class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(enabled=True)
    
class QuestionDetailView(DetailView):
    model = Question
    