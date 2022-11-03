
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from kmdb.pagination import CustomPageNumberPagination
from .permission import ReviewPermission, ReviewObjectPermission
from reviews.models import Review
from reviews.serializer import ReviewSerializer
from movies.models import Movie



class ReviewsViews(APIView, CustomPageNumberPagination): 

    authentication_classes = [TokenAuthentication]
    permission_classes = [ReviewPermission]


    def get(self, request: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        reviews = Review.objects.filter(movie_id=movie_id)

        result_page = self.paginate_queryset(reviews, request, view=self)
        
        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
    

    def post(self, request:Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        reviews = Review.objects.filter(movie_id=movie_id)

        for review in reviews:
            if review.user.id == request.user.id:
                return Response({"detail": "Review already exists."}, status.HTTP_403_FORBIDDEN)

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie = movie, user= request.user )

        return Response(serializer.data, status.HTTP_201_CREATED)



class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, ReviewObjectPermission]


    def get(self, request: Request, movie_id:int, review_id:int) -> Response: 
        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        serializer = ReviewSerializer(review)

        return Response(serializer.data)



    def delete(self, request: Request, movie_id:int, review_id:int) -> Response:
        review = get_object_or_404(Review, movie_id=movie_id, id=review_id)

        self.check_object_permissions(request, review)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)