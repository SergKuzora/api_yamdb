from rest_framework import serializers
from reviews.models import Comments, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text', 'author', 'score', 'pub_date')
        model = Review


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text', 'author', 'score', 'pub_date')
        model = Comments
