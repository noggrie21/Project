from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('detail/', views.user_detail),  # 유저 정보 조회, 수정, 삭제
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('watchedmovies/', views.watchedmovies),  # 이미 본 영화
    path('articles/', views.articles),  # 작성한 글 들
]

