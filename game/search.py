from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView
)

from .serializers import BasicGameSearchSerializer

from .document import GameDocument


class SearchGame(ListAPIView):
    serializer_class = BasicGameSearchSerializer

    def get_queryset(self, **kwargs):
        query = self.request.query_params.get('name', None)
        queryset = GameDocument.search()
        queryset = queryset.filter(
            'multi_match',
            query=query,
            fields=['name', 'description', 'category', 'id'],
            type='phrase_prefix'
        ) if query else queryset
        return queryset.execute()