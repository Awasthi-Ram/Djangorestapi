from rest_framework import serializers
from api1.models import Movie,collections

class  MovieSerializer(serializers.HyperlinkedModelSerializer):
    movie_id=serializers.ReadOnlyField()
    class Meta:
        model=Movie
        fields="__all__"


class collectionsSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model = collections
        fields='__all__'