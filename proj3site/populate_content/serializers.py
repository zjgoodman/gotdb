from rest_framework import serializers
from .models import Person, Castle, Region, House, Author


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region


class CastleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Castle


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House


