from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review, Comment

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email', 'nickname')
        read_only_fields = ('username', 'password',)


class UserWriteArticlesSerializer(serializers.ModelSerializer):

    class ReviewListSeiralizer(serializers.ModelSerializer):

        class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ('pk', 'title', )

        movie = MovieSerializer(read_only=True)
        
        class Meta:
            model = Review
            fields = ('content', 'created_at', 'updated_at', 'movie', 'liked_users') 


    class CommentSerializer(serializers.ModelSerializer):

        class ReviewSerializer(serializers.ModelSerializer):
            class Meta:
                model = Review
                fields = ('movie',)

        review = ReviewSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('content', 'created_at', 'updated_at', 'review',)

    comment_set = CommentSerializer(read_only=True, many=True)
    review_set = ReviewListSeiralizer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = ('username','review_set','comment_set',)
