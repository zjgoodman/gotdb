import string

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Castle, Region, Person
from .serializers import PeopleSerializer, RegionSerializer, CastleSerializer

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

def about_index(request):
    all_authors = Author.objects.all()
    context = {'all_authors': all_authors}
    return render(request, 'populate_content/about_index.html', context)

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


# API Views and JSON creator class
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def person_api_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JSONResponse(serializer.data)

def region_api_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return JSONResponse(serializer.data)

def castle_api_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        castle = Castle.objects.all()
        serializer = CastleSerializer(castle, many=True)
        return JSONResponse(serializer.data)

def person_api_detail(request, name):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        first_name, last_name = name.split('_')
        person = Person.objects.get(last_name__exact=last_name)
    except Person.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PeopleSerializer(person)
        return JSONResponse(serializer.data)

def region_api_detail(request, name):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        region = Region.objects.get(name__exact=name)
    except Region.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return JSONResponse(serializer.data)

def castle_api_detail(request, name):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        castle = Castle.objects.get(name__exact=name)
    except Castle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CastleSerializer(castle)
        return JSONResponse(serializer.data)
