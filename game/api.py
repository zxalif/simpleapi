from rest_framework.generics import ListAPIView

from .models import Game, ThreadImage, Thread
from .serializers import GameSerializer, ThreadSerializer


class GameView(ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        pk = self.request.query_params.get('id', None)
        queryset = queryset.filter(id=pk) if pk else queryset
        return queryset


class ThreadView(ListAPIView):
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()
