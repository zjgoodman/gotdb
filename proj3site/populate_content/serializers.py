from django.forms import widgets
from rest_framework import serializers
from .models import Person, Castle, Region

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'status', 'bio')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'capital_name', 'ruling_lord', 'description')

class CastleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Castle
        fields = ('id', 'name', 'region_name', 'ruling_lord', 'description')



