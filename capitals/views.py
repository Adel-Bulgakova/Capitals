from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from capitals.models import Capital
from random import randint

def results(request):
	if request.method == "GET":
		capital = get_object_or_404(Capital, pk = randint(0,20))
		return render(request, 'capitals/results.html', {'capital': capital})
	else:
		answer = request.POST["answer"]
		pk = request.POST["pk"]
		capital2 = get_object_or_404(Capital, pk = pk)
		if 	answer == capital2.answer:
			return render(request, 'capitals/success.html', {'lat': capital2.lat, 'lng': capital2.lng, 'capital':capital2})
		else:
			return render(request, 'capitals/fail.html', {'capital' : capital2})