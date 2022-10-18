from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie, Director, Actor, Review, Comment, Genre
from rest_framework.response import Response
from .serlializers.movies import MovieDetailSerializer, MovieListSerializer, RelatedMoviesSerializer, WatcheMovieSerializer
from .serlializers.review import ReviewSerializer, BestReviewSerializer
from .serlializers.comments import CommentSerializer
from .serlializers.genres import GenreSerializer, GenreDetailSerializer
from django.db.models import Count, Q
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta


# 장르 정보
@api_view(['GET'])
def genres(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(instance=genres, many=True)
    return Response(serializer.data)

# 베스트 댓글이 달리 영화
@api_view(['GET'])
def bestreviews(request):
    today = datetime.now()
    standard = today + timedelta(days=-1)
    reviews = Review.objects.filter(
        created_at__range=(f'{standard:%Y-%m-%d %H:%M}', f'{today:%Y-%m-%d %H:%M}')).annotate(
            like_count=Count('liked_users', distinct=True)).order_by(
                '-like_count','-created_at')[:5]
    serializers = BestReviewSerializer(reviews, many=True)
    return Response(serializers.data)


# 최신 개봉작 - 최신순
@api_view(['GET'])
def recent_new(request):
    user = request.user
    movielist = Movie.objects.exclude(watched_users__exact=user).order_by('-release_date')[:8]
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data)


# 최신 개봉작 - 인기순
@api_view(['GET'])
def recent_popular(request):
    user = request.user
    movielist = Movie.objects.exclude(watched_users__exact=user).order_by('-release_date', '-vote_average')[:8]
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data)


# 같은 개봉일
@api_view(['GET'])
def samedate(request):
    user = request.user
    today = datetime.today()
    month, day = today.month, today.day
    movielist = Movie.objects.filter(
        release_date__month=month,
        release_date__day=day).exclude(watched_users__exact=user)[:8]
    serializer = MovieListSerializer(movielist, many=True)
    return Response(serializer.data)


# 영화 디테일
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


# 감독의 다른 영화
@api_view(['GET'])
def directormovies(request, movie_id, director_id):
    director = get_object_or_404(Director, pk=director_id)
    movies = Movie.objects.filter(director=director).exclude(pk=movie_id)
    if movies.exists():
        serializer = RelatedMoviesSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        data = {
            "person": f"감독 {director.name}",
            "message" : "관련 영화 없음"
        }
        return Response(data)
    # 유저가 본 영화 필터링 필요


# 배우의 다른 영화
@api_view(['GET'])
def actormovies(request, movie_id, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    movies = actor.movies.all().exclude(pk=movie_id)
    if movies.exists():
        serializer = RelatedMoviesSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        data = {
            "person": f"{actor.name} 배우",
            "message" : "관련 영화 없음"
        }
        return Response(data)


# 영화 댓글(Review) 전체 조회 및 작성
@api_view(['POST', 'GET'])
def review_create(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)

    def review_create():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, movie=movie)

            reviews = movie.review_set.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def review_list():
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return review_create()


# 영화 댓글(Review) 수정 및 삭제
@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_id)

    def review_update():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.review_set.all()
                serializer = ReviewSerializer(reviews, many =True)
                return Response(serializer.data)

    def review_delete():
        if request.user == review.user:
            review.delete()
            reviews = movie.review_set.all()
            serializer = ReviewSerializer(reviews, many =True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return review_update()
    elif request.method == 'DELETE':
        return review_delete()


# 영화 댓글(Review) 좋아요
@api_view(['POST'])
def review_like(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user

    if review.liked_users.filter(pk=user.pk).exists():
        review.liked_users.remove(user)
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many =True)
        return Response(serializer.data)
    else:
        review.liked_users.add(user)
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many =True)
        return Response(serializer.data)


# 영화 이미 봤어요
@api_view(['POST'])
def movie_watch(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user

    if movie.watched_users.filter(pk=user.pk).exists():
        movie.watched_users.remove(user)
        movies = user.watching_movies.all()
        serializer = WatcheMovieSerializer(movies, many =True)
        return Response(serializer.data)
    else:
        movie.watched_users.add(user)
        movies = user.watching_movies.all()
        serializer = WatcheMovieSerializer(movies, many =True)
        return Response(serializer.data)


# 영화 대댓글(Comment) 작성
@api_view(['POST'])
def comment_create(request, movie_id, review_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_id)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, review=review)

        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 영화 대댓글(Comment) 수정 및 삭제
@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, movie_id, review_id, comment_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    def comment_update():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=user, review=review)

                reviews = movie.review_set.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def comment_delete():
        if request.user == comment.user:
            comment.delete()
            reviews = movie.review_set.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()

# 장르 포스터 
@api_view(['GET'])
def genredetail(request, genre_pk):
    user = request.user
    movies = Movie.objects.filter(genres=genre_pk).exclude(watched_users__exact=user).order_by('-vote_average')[:8]
    serializer = GenreDetailSerializer(movies, many=True)
    return Response(serializer.data)