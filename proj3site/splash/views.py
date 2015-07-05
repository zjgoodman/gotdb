from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader

def index(request):
    return render(request, 'splash/index.html')

