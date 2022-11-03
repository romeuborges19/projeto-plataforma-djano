from django.urls import path

import authors
from authors.views import question_page 
from . import views

urlpatterns = [
    path('question/<int:id>/', views.question, name="question-page"),
    path('question/ask/', authors.views.question_page, name="ask-page")
]
