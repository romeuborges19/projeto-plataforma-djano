from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('signup', views.register_page, name="signup"),
    path('signup/create/', views.register_create, name='create'),
    path('question/ask/', views.question_page, name='ask'),
    path('question/ask/create/', views.question_create, name='createask'),
]