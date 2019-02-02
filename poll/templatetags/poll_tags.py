from django import template
from django.template.loader import render_to_string
from django.utils.html import format_html
from poll.models import *
from poll import views
register = template.Library()


@register.simple_tag(takes_context=True)
def poll(context):
    request = context['request']

    try:
        question = Question.published.latest("date")
    except Poll.DoesNotExists:
        return ''

    items = Item.objects.filter(question=question)

    if poll.get_cookie_name() in request.COOKIES:
        template = "poll/result.html"
    else:
        template = "poll/poll.html"

    content = render_to_string(template, {
        'question': question,
        'items': items,
    })

    return content


@register.simple_tag                                                                                                                         
def percentage(question, item):
    print('question', question)
    question_vote_count = question.get_vote_count()
    if question_vote_count > 0:
        return float(item.get_vote_count()) / float(question_vote_count) * 100
