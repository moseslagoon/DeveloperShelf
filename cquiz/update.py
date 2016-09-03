from django.utils import timezone
import datetime
from .models import Question, Choice

def update():
    filename = 'question.txt'
    questions = []
    choices = []
    with open(filename) as my_file:
        for line in my_file:
            line = line.strip()
            if line.startswith('#'):
                currQ = Question(question_text=line, pub_date=timezone.now())
                questions.append(currQ)
            else:
                ans = Choice(choice_text=line, correct=True, question=currQ)
