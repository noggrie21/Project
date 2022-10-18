from rest_framework import serializers
from ..models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class GenreDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path', 'genres')