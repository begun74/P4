from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from polls.models import Choice, Question


def index(request):
    print('def index')
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    print('def detail')
    question = get_object_or_404(Question, pk=question_id)
    #print('question - ', question.pub_date)
    return render(request, 'polls/detail.html', {'question': question})