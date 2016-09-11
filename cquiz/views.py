from django.core.urlresolvers import  reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'cQuiz/base.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        :return:
        """
        return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'cQuiz/pieces/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'cQuiz/pieces/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'cQuiz/pieces/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice.correct:
            return HttpResponseRedirect(reverse('cquiz:results',
                                                args=(question.id,)))

        else:
            return render(request, 'cQuiz/pieces/detail.html', {
                'question': question,
                'error_message': "Wrong Answer, Try Again",
            })


        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.




"""
def index(request):
    context = {'mo_it': 'cQuiz', 'my_pages': ['Do 1', 'Do 2', 'Do 3', 'Do 4']}
    return render(request, 'cQuiz/base.html', context=context)
def qa(request):
    questions = Question.objects.all()
    context = {'mo_it': 'cQuiz', 'my_pages': ['Do 1', 'Do 2', 'Do 3', 'Do 4'], 'questions': questions}
    return render(request, 'cQuiz/tukra.html', context=context)
"""