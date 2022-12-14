from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
      'latest_question_list': latest_question_list,
  }
  return render(request,'polls/index.html', context)

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/index.html', {'question': question})

def result(request, question_id):
  response = "You are looking at the result of question %s"
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

# Create your views here.
