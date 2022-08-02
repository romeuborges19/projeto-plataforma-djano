from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    question_text = models.TextField()
    question_text_is_html = models.BooleanField(default=False)
    question_photo = models.ImageField(upload_to='questions/photos/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)