from rest_framework import serializers

from reviews.models import Comments, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['text', 'score']
        model = Review


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comments
