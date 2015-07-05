from django.contrib import admin

from .models import Person, Place, Region

admin.site.register(Person)
admin.site.register(Place)
admin.site.register(Region)
