# encoding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

from regular_app.models import Dog

from haystack import indexes
<<<<<<< HEAD
=======
from populate_content.models import Note, Person
>>>>>>> origin/matt


# More typical usage involves creating a subclassed `SearchIndex`. This will
# provide more control over how data is indexed, generally resulting in better
# search.
class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # We can pull data straight out of the model via `model_attr`.
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    # Note that callables are also OK to use.
    status = indexes.CharField(model_attr='status')
    # Note that we can't assign an attribute here. We'll manually prepare it instead.
    toys = indexes.MultiValueField()

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
<<<<<<< HEAD
        return self.get_model().objects.filter(public=True)

    # def prepare_toys(self, obj):
    #     # Store a list of id's for filtering
    #     return [toy.id for toy in obj.toys.all()]

        # Alternatively, you could store the names if searching for toy names
        # is more useful.
        # return [toy.name for toy in obj.toys.all()]
=======
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name  = indexes.CharField(model_attr='last_name', null=True)
    bio        = indexes.CharField(model_attr='bio')

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(status='Alive')
>>>>>>> origin/matt
