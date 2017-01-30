from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question, Choice

def details(request, id):
    quest = Question.objects.get(id=id)
    print quest
    allChoices = Choice.objects.filter(pQuest_id=id)
    print allChoices
    context = {'quest':quest,
               'allChoices':allChoices}
    return render(request, 'polls/details.html', context)

def showAllQuestions(request):
    allQuestions = Question.objects.all().order_by('pubDate')
    context = {'allQuestions':allQuestions}
    return render(request, 'polls/index.html', context)
