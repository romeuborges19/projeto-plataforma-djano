from django.contrib import admin
from .models import Answer, Category, Question
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

class QuestionAdmin(admin.ModelAdmin):
    ...

class AnswerAdmin(admin.ModelAdmin):
    ...

admin.site.register(Question, QuestionAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Answer, AnswerAdmin)