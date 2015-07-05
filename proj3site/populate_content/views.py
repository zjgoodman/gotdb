import string

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Person


def index(request):
    all_people = Person.objects.all()
    context = {'all_people': all_people}
    return render(request, 'populate_content/index.html', context)

def person_detail(request, person_name):
    try:
        first_name, last_name = person_name.split('_')
        person = Person.objects.get(last_name__exact=last_name)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")
    return render(request, 'populate_content/detail.html', {'person': person})

def test(request):
    return render(request, 'populate_content/www/index.html')
        

