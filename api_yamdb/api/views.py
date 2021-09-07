from django.shortcuts import get_object_or_404
from reviews.models import Review
from rest_framework import viewsets

from .serializers import CommentsSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('post_id'))
        serializer.save(review=review, author=self.request.user)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('post_id'))
        return review.comments.all()
