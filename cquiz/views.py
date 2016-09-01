from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'do_it': 'cQuized', 'my_pages': ['Do 1', 'Do 2', 'Do 3', 'Do 4']}
    return render(request, 'cQuiz/index.html', context = context)