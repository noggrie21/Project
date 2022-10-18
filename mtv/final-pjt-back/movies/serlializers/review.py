from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import  Review, Comment, Movie


User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    class CommentSerializer(serializers.ModelSerializer):
        
        class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model = User
                fields = ('pk', 'username',)
        
        user = UserSerializer(read_only=True)
        
        class Meta:
            model = Comment
            fields = ('pk', 'user', 'created_at', 'content',)

    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    liked_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'content', 'user', 'created_at', 'comment_set', 'liked_users', )
        read_only_fields = ('user','liked_users',)


class BestReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username',)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title',)

    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('like_count', 'content', 'user', 'movie', 'created_at',)