from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Person


def index(request):
    all_people = Person.objects.all()
    context = {'all_people': all_people}
    return render(request, 'populate_content/index.html', context)

def detail(request, last_name):
    try:
        person = Person.objects.get(last_name__exact=last_name)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")
    return render(request, 'populate_content/detail.html', {'person': person})

