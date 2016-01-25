from django.shortcuts import get_object_or_404, render

# Create your views here.

#if using render we dont need to load HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.template import loader
#from django.http import Http404
from django.views import generic

from .models import Choice, Question


'''

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template used for the long way
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list, 
	}
	return render(request, 'polls/index.html', context)
	#Long way below, shortcut above
	#return HttpResponse(template.render(context, request))


#THIS IS THE LONG WAY
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNowExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html',{'question':question})
	# Below the HttpResponse is used for the long response
	#return HttpResponse("You're looking at question %s." % question_id)


#SHORT WAY FOR 404'S:
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

'''

#THE ABOVE IS THE HARD WAY - WE ARE NOW USING GENERIC TEMPLATES:

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#Redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question':question,
			'error_message': "You didn't select a choice."
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button. BE CAREFUL TO INCLUDE THE COMMA IN ARGS
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
		

