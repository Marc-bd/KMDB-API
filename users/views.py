from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from users.permission import isAdminOrReadOnly, isAdminOrUser
from users.serializers import  UserSerializer
from .models import User
from kmdb.pagination import CustomPageNumberPagination



class UserViews(APIView, CustomPageNumberPagination): 
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrReadOnly]

    def get(self, request: Request) -> Response:

        users = User.objects.all()

        result_page= self.paginate_queryset(users, request, view=self)

        serializer = UserSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


    def post(self, request: Request) -> Response: 
        serializer = UserSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailViews(APIView): 

    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdminOrUser]

    def get(self, request:Request, user_id:int ) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data)


    