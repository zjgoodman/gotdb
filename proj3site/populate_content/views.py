import string

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Person, Region, Castle

def index(request):
    return render(request, 'splash/index.html')

def person_index(request):
    all_people = Person.objects.all()
    context = {'all_people': all_people}
    return render(request, 'populate_content/person_index.html', context)

def person_detail(request, person_name):
    try:
        first_name, last_name = person_name.split('_')
        person = Person.objects.get(last_name__exact=last_name)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")
    return render(request, 'populate_content/person_detail.html', {'person': person})

def region_index(request):
    all_regions = Region.objects.all()
    context = {'all_regions': all_regions}
    return render(request, 'populate_content/region_index.html', context)

def region_detail(request, region_name):
    try:
        region = Region.objects.get(name__exact=region_name)
    except Region.DoesNotExist:
        raise Http404("Region does not exist :")
    return render(request, 'populate_content/region_detail.html', {'region': region})

def castle_index(request):
    all_castles = Castle.objects.all()
    context = {'all_castles': all_castles}
    return render(request, 'populate_content/castle_index.html', context)

def castle_detail(request, castle_name):
    try:
        castle = Castle.objects.get(name__exact=castle_name)
    except Castle.DoesNotExist:
        raise Http404("Castle does not exist :")
    return render(request, 'populate_content/castle_detail.html', {'castle': castle})
