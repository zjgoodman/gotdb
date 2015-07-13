from rest_framework import serializers
from .models import Person, Castle, Region, House, Author


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'person_id', 'first_name', 'last_name', 'house_name', 'region_from', 'titles', 'actor', 'status', 'bio')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'region_id', 'name', 'capital_name', 'ruling_house', 'ruling_lord', 'description', 'history')


class CastleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Castle
        fields = ('id', 'castle_id', 'name', 'region_name', 'ruling_house', 'ruling_lord', 'description', 'history')


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'house_id', 'name', 'words', 'region_name', 'castle_name', 'description', 'people')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'author_id',
                  'first_name',
                  'last_name',
                  'bio',
                  'responsibilities',
                  'num_commits',
                  'num_issues',
                  'num_unit_tests')

