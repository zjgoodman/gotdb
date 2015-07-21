from django.utils.html import format_html_join
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
import string, re, subprocess, os

from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Castle, Region, Person, House, Author
from .serializers import PeopleSerializer, RegionSerializer, CastleSerializer, HouseSerializer

from .models import Person, Region, Castle

def index(request):
    return render(request, 'splash.html')

def about(request):
    all_authors = Author.objects.all()
    context = {'all_authors': all_authors}
    return render(request, 'about.html', context)

def unit_tests(request):
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))

	command = "python3 " + os.path.join(BASE_DIR, 'manage.py') + " test populate_content -v 2 --keepdb"
	pipe = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	result = pipe.stdout.readlines() + pipe.stderr.readlines()
	return render_to_response('unit_tests.html', {'result': result})

def person_index(request):
    all_objects = Person.objects.all()
    context = {'all_objects': all_objects, 'title': "People"}
    return render(request, 'model_list.html', context)

def person_detail(request, person_id):
    try:
        person = Person.objects.get(person_id__exact=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")

    description = person.bio
    for h in House.objects.all():
        regex = re.compile("%s" % str(h))
        description = regex.sub(r'<a href="/houses/%s/">%s</a>' % (h.get_id(), str(h)), description)

    for p in Person.objects.all():
        if str(p) != str(person):
            regex = re.compile("%s" % str(p))
            description = regex.sub(r'<a href="/people/%s/">%s</a>' % (p.get_id(), str(p)), description)

    for c in Castle.objects.all():
        regex = re.compile("%s" % str(c))
        description = regex.sub(r'<a href="/castles/%s/">%s</a>' % (c.get_id(), str(c)), description)

    for r in Region.objects.all():
        regex = re.compile("%s" % str(r))
        description = regex.sub(r'<a href="/regions/%s/">%s</a>' % (r.get_id(), str(r)), description)

    context = {'person'  : person,
               'bio'     : description,
               'castles' : person.castles_controlled.all(),}
    return render(request, 'person_detail.html', context)

def region_index(request):
    all_objects = Region.objects.all()
    context = {'all_objects': all_objects, 'title': "Regions"}
    return render(request, 'model_list.html', context)

def region_detail(request, region_id):
    try:
        region = Region.objects.get(region_id__exact=region_id)
    except Region.DoesNotExist:
        raise Http404("Region does not exist :")

    description = region.description
    history     = region.history
    for h in House.objects.all():
        regex = re.compile("%s" % str(h))
        description = regex.sub(r'<a href="/houses/%s/">%s</a>' % (h.get_id(), str(h)), description)
        history     = regex.sub(r'<a href="/houses/%s/">%s</a>' % (h.get_id(), str(h)), history)

    for p in Person.objects.all():
        regex = re.compile("%s" % str(p))
        description = regex.sub(r'<a href="/people/%s/">%s</a>' % (p.get_id(), str(p)), description)
        history     = regex.sub(r'<a href="/people/%s/">%s</a>' % (p.get_id(), str(p)), history)

    for c in Castle.objects.all():
        regex = re.compile("%s" % str(c))
        description = regex.sub(r'<a href="/castles/%s/">%s</a>' % (c.get_id(), str(c)), description)
        history     = regex.sub(r'<a href="/castles/%s/">%s</a>' % (c.get_id(), str(c)), history)

    for r in Region.objects.all():
        if r.name != region.name:
            regex = re.compile("%s" % str(r))
            history = regex.sub(r'<a href="/regions/%s/">%s</a>' % (r.get_id(), str(r)), history)
            description = regex.sub(r'<a href="/regions/%s/">%s</a>' % (r.get_id(), str(r)), description)

    context = {'region'     : region,
               'castles'    : region.other_castles.all(),
               'description': description,
               'history'    : history,
              }
    return render(request, 'region_detail.html', context)

def castle_index(request):
    all_objects = Castle.objects.all()
    context = {'all_objects': all_objects, 'title': "Castles"}
    return render(request, 'model_list.html', context)

def castle_detail(request, castle_id):
    try:
        castle = Castle.objects.get(castle_id__exact=castle_id)
    except Castle.DoesNotExist:
        raise Http404("Castle does not exist :")

    description = castle.description
    history     = castle.history
    for h in House.objects.all():
        regex = re.compile("%s" % str(h))
        description = regex.sub(r'<a href="/houses/%s/">%s</a>' % (h.get_id(), str(h)), description)
        history     = regex.sub(r'<a href="/houses/%s/">%s</a>' % (h.get_id(), str(h)), history)

    for p in Person.objects.all():
        regex = re.compile("%s" % str(p))
        description = regex.sub(r'<a href="/people/%s/">%s</a>' % (p.get_id(), str(p)), description)
        history     = regex.sub(r'<a href="/people/%s/">%s</a>' % (p.get_id(), str(p)), history)

    for c in Castle.objects.all():
        if c.name != castle.name:
            regex = re.compile("%s" % str(c))
            description = regex.sub(r'<a href="/castles/%s/">%s</a>' % (c.get_id(), str(c)), description)
            history     = regex.sub(r'<a href="/castles/%s/">%s</a>' % (c.get_id(), str(c)), history)

    for r in Region.objects.all():
        regex = re.compile("%s" % str(r))
        history = regex.sub(r'<a href="/regions/%s/">%s</a>' % (r.get_id(), str(r)), history)
        description = regex.sub(r'<a href="/regions/%s/">%s</a>' % (r.get_id(), str(r)), description)

    context = {'castle'     : castle,
               'description': description,
               'history': history,
              }
    return render(request, 'castle_detail.html', context)

def house_index(request):
    all_objects = House.objects.all()
    context = {'all_objects': all_objects, 'title': "Houses"}
    return render(request, 'model_list.html', context)

def house_detail(request, house_id):
    try:
        house = House.objects.get(house_id__exact=house_id)
    except House.DoesNotExist:
        raise Http404("House does not exist :")

    description = house.description
    for h in House.objects.all():
        if h.name != house.name:
            regex = re.compile("%s" % str(h))
            description = regex.sub(r'<a href="/houses/%s/">%s</a>' % (h.get_id(), str(h)), description)

    for p in Person.objects.all():
        regex = re.compile("%s" % str(p))
        description = regex.sub(r'<a href="/people/%s/">%s</a>' % (p.get_id(), str(p)), description)

    for c in Castle.objects.all():
        regex = re.compile("%s" % str(c))
        description = regex.sub(r'<a href="/castles/%s/">%s</a>' % (c.get_id(), str(c)), description)

    for r in Region.objects.all():
        regex = re.compile("%s" % str(r))
        description = regex.sub(r'<a href="/regions/%s/">%s</a>' % (r.get_id(), str(r)), description)

    context = {'house'      : house, 
               'people'     : house.members.all(), 
               'description': description,
               'castles'    : house.castles_controlled.all(),}

    return render(request, 'house_detail.html', context)

def all_castles_index(request):
    all_castles = Castle.objects.all()
    context = {'all_castles': all_castles}
    return render(request, 'all_castles_index.html', context)

def all_people_index(request):
    all_people = Person.objects.all()
    context = {'all_people': all_people}
    return render(request, 'all_people_index.html', context)

def all_regions_index(request):
    all_regions = Region.objects.all()
    context = {'all_regions': all_regions}
    return render(request, 'all_regions_index.html', context)

def all_houses_index(request):
    all_houses = House.objects.all()
    context = {'all_houses': all_houses}
    return render(request, 'all_houses_index.html', context)


#--------------------------------------------------------------------------------
#                           API STUFF
#--------------------------------------------------------------------------------

# JSON creator class
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data, renderer_context={'indent':4})
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#List all items.
def person_api_list(request):
    """
    List all people (characters).
    """
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JSONResponse(serializer.data)

def region_api_list(request):
    """
    List all regions.
    """
    if request.method == 'GET':
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return JSONResponse(serializer.data)

def castle_api_list(request):
    """
    List all castles.
    """
    if request.method == 'GET':
        castle = Castle.objects.all()
        serializer = CastleSerializer(castle, many=True)
        return JSONResponse(serializer.data)

def house_api_list(request):
    """
    List all houses.
    """
    if request.method == 'GET':
        house = House.objects.all()
        serializer = HouseSerializer(house, many=True)
        return JSONResponse(serializer.data)

#List a specific item

def person_api_detail(request, person_id):
    """
    Retrieve a specific person.
    """
    try:
        person = Person.objects.get(person_id__exact=person_id)
    except Person.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PeopleSerializer(person)
        return JSONResponse(serializer.data)

def region_api_detail(request, region_id):
    """
    Retrieve a specific region.
    """
    try:
        region = Region.objects.get(region_id__exact=region_id)
    except Region.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return JSONResponse(serializer.data)

def castle_api_detail(request, castle_id):
    """
    Retrieve a specific castle.
    """
    try:
        castle = Castle.objects.get(castle_id__exact=castle_id)
    except Castle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CastleSerializer(castle)
        return JSONResponse(serializer.data)

def house_api_detail(request, house_id):
    """
    Retrieve a specific house.
    """
    try:
        house = House.objects.get(house_id__exact=house_id)
    except House.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HouseSerializer(house)
        return JSONResponse(serializer.data)

