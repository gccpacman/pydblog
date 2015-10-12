from django.shortcuts import HttpResponse
from django.template import loader, RequestContext

from polls.models import Question


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    content = RequestContext(request, {
        'latest_question_list': question_list
    })
    return HttpResponse(template.render(content))


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    template = loader.get_template('polls/details.html')
    content = RequestContext(request, {
        'question': question
    })
    return HttpResponse(template.render(content))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
