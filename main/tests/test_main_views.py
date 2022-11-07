from django.test import TestCase
from django.urls import reverse, resolve
from main import views
import authors.views

class QuestionViewsTest(TestCase):
    def test_home_views_function_is_correct(self):
        view = resolve(reverse('home-page'))
        self.assertIs(view.func, views.home)
    
    def test_question_views_function_is_correct(self):
        view = resolve(reverse('question-page', kwargs={'id': 1}))
        self.assertIs(view.func, views.question)
    
    def test_asking_views_function_is_correct(self):
        view = resolve(reverse('main:ask-page'))
        self.assertIs(view.func, authors.views.question_page)

    def test_asking_views_function_is_correct(self):
        view = resolve(reverse('authors:createask'))
        self.assertIs(view.func, authors.views.question_create)

    def test_home_view_return_status_code_200_OK(self):
        response = self.client.get(reverse('home-page'))
        ...
