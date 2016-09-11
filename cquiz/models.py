from django.db import models

import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    q_id = models.IntegerField(default=0)

    def __str__(self):
        return "{0}. {1}".format(self.q_id, self.question_text)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    correct = models.BooleanField(default=False)
    c_id = models.IntegerField(default=0)

    def __str__(self):
        return "{0} {1} {2} ".format(self.question.q_id, self.c_id, self.choice_text)
