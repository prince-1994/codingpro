from django.shortcuts import render

from .models import Question, Platform, Solution, Language, Topic

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
    'questions' : questions,
  }
  return render(request, "solutionblog/frontpage.html", context)

def topicpage(request, topicId):
  topic = Topic.objects.get(pk=topicId)
  questions = topic.questions.all()
  context = {
    'questions' : questions,
  }
  return render(request, "solutionblog/frontpage.html", context)

def detail(request, questionId):
  question = Question.objects.get(pk=questionId)
  context = {
    'question' : question
  }
  return render(request, "solutionblog/detail.html", context)