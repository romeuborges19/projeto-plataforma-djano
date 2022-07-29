from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'main/pages/home.html')

def question(request, id):
    return render(request, 'main/pages/question-view.html')