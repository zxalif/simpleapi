from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Game


@registry.register_document
class GameDocument(Document):

    class Index:
        name = 'games'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    class Django:
        model = Game
        fields = [
            'name',
            'image',
            'description',
        ]