from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('signup', views.register_page, name="signup"),
    path('signup/create/', views.register_create, name='create')
]