from django.shortcuts import render

from .models import Question, Platform, Solution, Language

def frontpage(request):
  questions = Question.objects.all()
  context = {
    'questions' : questions
  }
  return render(request, "solutionblog/frontpage.html", context)

def platformpage(request, platformId):
  platform = Platform.objects.get(pk=platformId)
  questions = platform.questions.all()
  context = {
    'questions' : questions
  }
  return render(request, "solutionblog/frontpage.html", context)

def detail(request, id):
  question = Question.objects.get(pk=id)
  context = {
    'question' : question
  }
  return render(request, "solutionblog/detail.html", context)