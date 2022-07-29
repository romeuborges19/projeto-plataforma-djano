from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from authors.forms import CreateUserForm
from django.http import Http404, HttpResponse

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
    return redirect('authors:signup')