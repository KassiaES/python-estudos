from django.contrib import admin
from django.urls import path, include 
from .views import QuestionListView, QuestionDetailView, VoteCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question-detail"),
    path("<int:pk>/vote", VoteCreateView.as_view(), name="question-vote"),
]
