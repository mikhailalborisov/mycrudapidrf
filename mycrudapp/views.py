from rest_framework import viewsets, mixins
from .models import Film
from .serializers import FilmSerializer


class FilmViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    queryset = Film.objects.all()


    serializer_class = FilmSerializer