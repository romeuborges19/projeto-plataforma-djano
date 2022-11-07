from django.test import TestCase
from django.urls import reverse

class QuestionURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('home-page')
        self.assertEqual(url, '/')
    
    def test_question_url_is_correct(self):
        url = reverse('question-page', kwargs={'id': 1})
        self.assertEqual(url, '/question/1/')