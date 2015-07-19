import datetime
from haystack import indexes
from populate_content.models import Person, Castle, Region, House

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # first_name = indexes.CharField(model_attr='first_name')
    # last_name  = indexes.CharField(model_attr='last_name', null=True)

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
         return self.get_model()._default_manager.all()

class HouseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # name = indexes.CharField(model_attr='name')

    def get_model(self):
        return House

    def index_queryset(self, using=None):
         return self.get_model()._default_manager.all()

class CastleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Castle

    def index_queryset(self, using=None):
         return self.get_model()._default_manager.all()

class RegionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Region

    def index_queryset(self, using=None):
         return self.get_model()._default_manager.all()