from django.conf.urls import patterns, url

from capitals import views

urlpatterns = patterns ('',
 	url(r'^capital/$', views.results),
)