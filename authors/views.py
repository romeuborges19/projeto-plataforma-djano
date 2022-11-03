from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from authors.forms import CreateUserForm, QuestionForm
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.


def register_page(request):
    register_form_data = request.session.get('register_form_data', None)

    form = CreateUserForm(register_form_data)
    context = {'form': form}
    return render(request, 'authors/pages/register_page.html', context)

def register_create(request):
    if not request.POST:
        raise Http404('teste')

    POST = request.POST
    request.session['register_form_data'] = POST

    form = CreateUserForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário criado. Por favor, faça login.')

        del(request.session['register_form_data'])

    return redirect('authors:signup')

def question_page(request):
    question_form_data = request.session.get('question_form_data', None)
    form = QuestionForm(question_form_data)
    context = {'form': form}
        
    return render(request, 'authors/pages/question_form.html', context)

def question_create(request):

    if not request.POST:
        raise Http404('teste')
    
    POST = request.POST
    request.session['question_form_data'] = POST

    form = QuestionForm(request.POST)

    if form.is_valid():
        form.save()
    
    return redirect('home-page')