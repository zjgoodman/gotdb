from django.contrib import admin

from .models import Person, Region, Castle, House, Author, Note

admin.site.register(Person)
admin.site.register(Region)
admin.site.register(Castle)
admin.site.register(House)
admin.site.register(Author)
admin.site.register(Note)
