from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Choice, Question
# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list':latest_question_list}
  #render template using context dictionary
  return render(request, 'polls/index.html', context)

  #load a template manually
  #template = loader.get_template('polls/index.html')
  #render templtae using the context objctt
  #return HttpResponse(template.render(context))

def detail(request, question_id):
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
  question = get_object_or_404(Question,pk=question_id)
  return render(request, 'polls/detail.html',{'question':question})




def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
  p = get_object_or_404(Question, pk=question_id)
  try:
    #request.POST['var'] lets u get from post variables
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(request, 'polls/detail.html', {
      'question': p,
      'error_message': "You didn't select a choice.",
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    #  reverse will find the path to the view you want to show
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
