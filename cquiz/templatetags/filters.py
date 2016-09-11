from django import template
from cquiz.models import Choice

register = template.Library()


@register.filter
def get_choices(question):
    return Choice.objects.filter(question=question)[0].choice_text

@register.filter
def increment_me(num):
    return num+1