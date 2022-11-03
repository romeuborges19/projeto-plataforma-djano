from unicodedata import category
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Question, Answer, Category

class QuestionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={'class':'question-category-form-control'}),
        label='question-category',
    )

    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(
            attrs={'class':'question-category-form-control'}),
        label='question-category',
    )
    class Meta:
        model = Question
        fields = ['title', 'question_text', 'question_photo', 'category']

    title = forms.CharField(
        label='title',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    question_photo = forms.ImageField(

    )

    question_text = forms.CharField(
        widget=forms.TextInput(attrs={'class':'question-body-form-control'}),
        label='question_text',
        error_messages={
            'required':'O corpo da pergunta não pode estar vazio',
        }
    )

    

class CreateUserForm(UserCreationForm):

    username=forms.CharField(
        error_messages={
            'required':'Insira um nome de usuário.',
            'max_lenght':'O nome de usuário não pode ter mais que 150 caracteres',
            'min_length':'O nome de usuário deve ter pelo menos 4 caracteres',
        },
        label='username',
        max_length=150,
        min_length=4,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    email=forms.CharField(
        error_messages={'required':'Insira seu e-mail'},
        label='email',
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    password1= forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control', 
            'style':'width: 420px; height: 30px; padding-inline: 10px;'}),
        error_messages={'required':'Este campo é obrigatório'},
        label='password1',
    )

    password2= forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control',
            'style':'width: 420px; height: 30px; padding-inline: 10px;'}),
        error_messages={'required':'Este campo é obrigatório'},
        label='password2',
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
