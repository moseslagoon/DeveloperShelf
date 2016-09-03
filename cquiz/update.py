import os
from django.utils import timezone
from .models import Question, Choice

def update():
    module_dir = os.path.dirname(__file__)
    filename = os.path.join(module_dir, 'questions.txt')
    questions = []
    choices = []
    with open(filename) as my_file:
        q_counter = 0
        c_counter = 0
        for line in my_file:
            line = line.strip()
            if line.startswith('#'):
                line = line.replace('#', "")
                q_counter += 1
                c_counter=0
                currQ = Question(question_text=line, pub_date=timezone.now(), q_id=q_counter)
                questions.append(currQ)
            else:
                c_counter += 1
                ans = Choice(choice_text=line, correct=True, question=questions[len(questions)-1], c_id=c_counter)
                choices.append(ans)
    return questions, choices

def  update_choice():
    module_dir = os.path.dirname(__file__)
    filename = os.path.join(module_dir, 'questions.txt')
    questions = Question.objects.all()
    answers = []
    with open(filename) as myfile:
        q_counter = 0
        c_counter = 0
        for line in myfile:
            line = line.strip()
            if line.startswith("#"):
                q_counter += 1
                c_counter = 0
            else:
                c_counter += 1
                answer = Choice(choice_text=line, correct=True, question=questions[q_counter-1], c_id=c_counter)
                answers.append(answer)
    return answers