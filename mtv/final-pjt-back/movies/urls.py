from django.urls import path
from . import views

urlpatterns = [
    # 영화 봤어요
    path('movies/<int:movie_id>/watch/', views.movie_watch),

    # 장르 정보
    path('movies/genres/', views.genres),
    path('movies/genredetail/<int:genre_pk>/', views.genredetail),
    
    # 베스트 리뷰
    path('movies/bestreviews/', views.bestreviews),

    # 최신 개봉작 추천
    path('movies/recent-new/', views.recent_new),
    path('movies/recent-popular/', views.recent_popular),

    # 같은 개봉일 추천
    path('movies/samedate/', views.samedate),

    # 영화 상세 정보
    path('movies/<int:movie_id>/', views.movie_detail),

    # 영화 감독 및 배우 다른 작품
    path('movies/<int:movie_id>/director/<int:director_id>/', views.directormovies),
    path('movies/<int:movie_id>/actor/<int:actor_id>/', views.actormovies),

    # 댓글(Review) 작성(조회) 및 수정
    path('movies/<int:movie_id>/review/', views.review_create),
    path('movies/<int:movie_id>/review/<int:review_id>/', views.review_update_or_delete),
    # 댓글 좋아요
    path('movies/<int:movie_id>/review/<int:review_id>/like/', views.review_like),

    # 대댓글(Comment)
    path('movies/<int:movie_id>/review/<int:review_id>/comment/', views.comment_create),
    path('movies/<int:movie_id>/review/<int:review_id>/comment/<int:comment_id>/', views.comment_update_or_delete),
]
