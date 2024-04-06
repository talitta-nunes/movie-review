
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from reviews.permissions import DeletePermission, PostPermission
from movies.models import Movie

from .models import Review
from .serializers import ReviewSerializer


class ReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [PostPermission]

    def post(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, id=movie_id)

        serializer = ReviewSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie, critic=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, movie_id: int) -> Response:

        reviews = Review.objects.filter(movie_id=movie_id)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DeletePermission]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:

        reviewMovie = get_object_or_404(
            Review, movie_id=movie_id, id=review_id
        )

        serializer = ReviewSerializer(reviewMovie)

        return Response(serializer.data)

    def delete(
        self, request: Request, movie_id: int, review_id: int
    ) -> Response:

        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
