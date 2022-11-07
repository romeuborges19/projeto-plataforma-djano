import authors
from django.urls import path
from authors import views
from . import views

app_name = 'main'

urlpatterns = [
    path('question/<int:id>/', views.question, name="question-page"),
]
