from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'do_it': 'cQuized', 'my_dropdowns': ['d1', 'd2', 'd3', 'd4'],
               'my_pages': ['Page 1', 'Page 2', 'Page 3', 'Page 4']}

    return render(request, 'cQuiz/index.html', context = context)