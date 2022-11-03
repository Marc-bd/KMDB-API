from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Review

class ReviewPermission(permissions.BasePermission):
    
       def has_permission(self, request: Request, view:View):

        return ( request.method == "GET" or request.user.is_superuser or request.user.is_critic)

       
  

class ReviewObjectPermission(permissions.BasePermission):

    def has_object_permission(self, request:Request, view: View, obj: Review):

       
        return(
           request.method == "GET" or request.user.is_superuser or request.user.id == obj.user.id
        )
       