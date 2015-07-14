from django.utils.html import format_html_join
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
import string, re

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Castle, Region, Person, House, Author
from .serializers import PeopleSerializer, RegionSerializer, CastleSerializer, HouseSerializer

from .models import Person, Region, Castle


def index(request):
    return render(request, 'splash/index.html')

def about_index(request):
    all_authors = Author.objects.all()
    context = {'all_authors': all_authors}
    return render(request, 'populate_content/about_index.html', context)

def person_index(request):
    all_people = Person.objects.all()
    context = {'all_people': all_people}
    return render(request, 'populate_content/person_index.html', context)

def person_detail(request, person_id):
    try:
        person = Person.objects.get(person_id__exact=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist :")
    context = {'person': person,
               'bio'   : format_html_join('\n', '<p>{0}</p>', ((force_text(p),) for p in re.split("<p>|</p>", person.bio))),}
    return render(request, 'populate_content/person_detail.html', context)

def region_index(request):
    all_regions = Region.objects.all()
    context = {'all_regions': all_regions}
    return render(request, 'populate_content/region_index.html', context)

def region_detail(request, region_id):
    try:
        region = Region.objects.get(region_id__exact=region_id)
    except Region.DoesNotExist:
        raise Http404("Region does not exist :")
    context = {'region'     : region,
               'description': format_html_join('\n', '<p>{0}</p>', ((force_text(p),) for p in re.split("<p>|</p>", region.description))),
               'history': format_html_join('\n', '<p>{0}</p>', ((force_text(p),) for p in re.split("<p>|</p>", region.history))),
              }
    return render(request, 'populate_content/region_detail.html', context)

def castle_index(request):
    all_castles = Castle.objects.all()
    context = {'all_castles': all_castles}
    return render(request, 'populate_content/castle_index.html', context)

def castle_detail(request, castle_id):
    try:
        castle = Castle.objects.get(castle_id__exact=castle_id)
    except Castle.DoesNotExist:
        raise Http404("Castle does not exist :")
    context = {'castle'     : castle,
               'description': format_html_join('\n', '<p>{0}</p>', ((force_text(p),) for p in re.split("<p>|</p>", castle.description))),
               'history': format_html_join('\n', '<p>{0}</p>', ((force_text(p),) for p in re.split("<p>|</p>", castle.history))),
              }
    return render(request, 'populate_content/castle_detail.html', context)

def house_index(request):
    all_houses = House.objects.all()
    context = {'all_houses': all_houses}
    return render(request, 'populate_content/house_index.html', context)

def house_detail(request, house_id):
    try:
        house = House.objects.get(house_id__exact=house_id)
    except House.DoesNotExist:
        raise Http404("House does not exist :")
    context = {'house'      : house, 
               'people'     : house.members.all(), 
               'description': format_html_join('\n', '<p>{0}</p>', ((force_text(p),) for p in re.split("<p>|</p>", house.description)))}

    return render(request, 'populate_content/house_detail.html', context)

def all_castles_index(request):
    all_castles = Castle.objects.all()
    context = {'all_castles': all_castles}
    return render(request, 'populate_content/all_castles_index.html', context)

def all_people_index(request):
    all_people = Person.objects.all()
    context = {'all_people': all_people}
    return render(request, 'populate_content/all_people_index.html', context)

def all_regions_index(request):
    all_regions = Region.objects.all()
    context = {'all_regions': all_regions}
    return render(request, 'populate_content/all_regions_index.html', context)

def all_houses_index(request):
    all_houses = House.objects.all()
    context = {'all_houses': all_houses}
    return render(request, 'populate_content/all_houses_index.html', context)


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

