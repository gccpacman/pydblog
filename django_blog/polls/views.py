from __future__ import absolute_import, unicode_literals
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.template import loader, RequestContext

from polls.models import Question, Choice


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
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponse("You're voting on question %s." % question_id)


def bootstrap(request):
    return render(request, 'polls/bootstrap.html', {})


def login(request):
    return render(request, 'blog/index.html', {})
