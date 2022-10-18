from rest_framework import serializers
from movies.models import Actor, Director, Movie, Genre, Review


class WatcheMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'release_date', 'poster_path',)


# (감독 및 배우) 관련 영화 시리얼라이저
class RelatedMoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'poster_path', 'title')


# 최신 개봉작 추천(메인 페이지) 시리얼라이저
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'poster_path', 'release_date', 'title')



# 영화 디테일 시리얼 라이져
class MovieDetailSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id', 'name', 'profile_path')
    
    class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('id', 'name', 'profile_path')


    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'vote_average', 'poster_path', 'release_date', 
        'genres', 'director', 'actors',)

