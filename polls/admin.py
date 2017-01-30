from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceCustom(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionCustom(admin.ModelAdmin):
    inlines = [ChoiceCustom]

class QuestionCustom2(admin.ModelAdmin):
    inlines = [ChoiceCustom]
    list_display = ('qText','pubDate', 'isPublishedBeforeToday')

    search_fields = ['qText']
    list_filter = ['pubDate']

admin.site.register(Choice)
admin.site.register(Question, QuestionCustom2)
