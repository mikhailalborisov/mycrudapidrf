from rest_framework import serializers

from mycrudapp.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'name', 'genre', 'director', 'release_date')
        # read_only_fields = ('name', 'genre', )
