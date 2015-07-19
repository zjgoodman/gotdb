import datetime
from haystack import indexes
from .models import Note, Person


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
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
        return self.get_model().objects.filter(status='Dead')