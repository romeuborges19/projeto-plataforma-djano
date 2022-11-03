from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer, Question

from utils.main.factory import make_question

#página principal
def home(request):

    questions = Question.objects.filter(
        is_published = True
    ).order_by('-id')

    return render(request, 'main/pages/home.html', 
    context={'questions': questions},
    )

#página de cada pergunta
def question(request, id):
    question = Question.objects.filter(
        id = id,
    ).order_by('-id').first()

    answers = Answer.objects.all()

    if not question:
        return HttpResponse(content = 'Not found', status = 404)

    return render(request, 'main/pages/question-view.html', 
        context={
            'question': question, 
            'answers': answers,
            'is_detail_page': True,
            'title': f'{question.title}'
        }
    )