import string

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import PeopleSerializer

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

<<<<<<< HEAD
=======
def test(request):
    return render(request, 'populate_content/www/index.html')

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def person_api_list(request):
    """
    List all characters.
    """
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PeopleSerializer(person, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def person_api_detail_name(request, person_name):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        first_name, last_name = person_name.split('_')
        person = Person.objects.get(last_name__exact=last_name)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")

    if request.method == 'GET':
        serializer = PeopleSerializer(person)
        return JSONResponse(serializer.data)


def person_api_detail_pk(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")

    if request.method == 'GET':
        serializer = PeopleSerializer(person)
        return JSONResponse(serializer.data)
        

>>>>>>> 5f1ae4589a6ecb195dd29220da61ae674b685173
