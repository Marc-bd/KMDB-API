from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from .models import Movie
from .serializers import MovieSerializer
from .permission import isAdminOrReadOnly
from django.shortcuts import get_object_or_404
from kmdb.pagination import CustomPageNumberPagination


class MoviesViews(APIView, CustomPageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrReadOnly]
    

    def get(self, request: Request) ->  Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)
    

    def post(self, request: Request) -> Response:

        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()


        return Response(serializer.data, status.HTTP_201_CREATED)


class MoviesDetailViews(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrReadOnly]


    def get(self, request: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        
     
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    

    def delete(self, request: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request: Request, movie_id:int) -> Response:
         movie = get_object_or_404(Movie, id=movie_id)

         serializer =  MovieSerializer(movie, data=request.data, partial=True)

         serializer.is_valid(raise_exception=True)

         serializer.save()

         return Response(serializer.data)
