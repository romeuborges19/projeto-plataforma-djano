from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from utils.main.factory import make_question

# Create your views here.

def home(request):
    return render(request, 
    'main/pages/home.html', 
    context={'questions': [make_question() for _ in range(10)]},
    )

def question(request, id):
    return render(request, 'main/pages/question-view.html', context={'question': make_question()})