from django.conf.urls import url

from . import views

app_name='polls' #this allows reference like: <a href="{% url 'polls:detail' question.id %}"> in the index.html (template)


'''
urlpatterns = [
	# ex: /polls/
	url(r'^$',views.index, name="index"),
	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$',views.detail, name="detail"),
	# ex: /polls/5/results
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	# ex: /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
'''

#Now using the django generic templates

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]