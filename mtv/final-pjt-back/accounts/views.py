from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserWriteArticlesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.models import Movie
from movies.serlializers.movies import WatcheMovieSerializer
from django.contrib.auth import get_user_model

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request):
    # 요청한 user에 대한 정보를 user에 담는다.
    user = request.user

    def detail_user():
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update_user():
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete_user():
        if user.is_authenticated:   # 로그인 했는지 안했는지
            user.delete()
            return Response({'message': '삭제 완료'})

    if request.method == 'GET':
        return detail_user()
    elif request.method == 'PUT':
        return update_user()
    elif request.method == 'DELETE':
        
        return delete_user()


# 프로필 페이지 접속 시 본 영화 목록 받아올 api
@api_view(['GET'])
def watchedmovies(request):
    user = request.user
    movielist = Movie.objects.filter(watched_users__exact=user)
    serializer = WatcheMovieSerializer(movielist, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def articles(request):
    user = get_object_or_404(get_user_model(), username=request.user.username)
    serializer = UserWriteArticlesSerializer(instance=user)
    return Response(serializer.data)

