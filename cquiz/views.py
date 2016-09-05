from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    context = {'do_it': 'cQuized', 'my_dropdowns': ['d1', 'd2', 'd3', 'd4'],
               'my_pages': ['Page 1', 'Page 2', 'Page 3', 'Page 4']}

    return render(request, 'cQuiz/base.html', context = context)

def qa(request):
    question = Question.objects.all()
    ans = Choice.objects.all()
    context = {'do_it': 'cQuized', 'my_dropdowns': ['d1', 'd2', 'd3', 'd4'],
               'my_pages': ['Page 1', 'Page 2', 'Page 3', 'Page 4'], 'question': question,
               'ans': ans}
    return render(request, 'cQuiz/form.html', context=context)