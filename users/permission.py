from rest_framework.views import Request, View
from rest_framework import permissions
import ipdb
from users.models import User



class isAdminOrReadOnly(permissions.BasePermission):


    def has_permission(self, request: Request, view: View):


        return (request.method == "POST" or request.user.is_authenticated and request.user.is_superuser)




class isAdminOrUser(permissions.BasePermission):
    
    def has_object_permission(self, request: Request, view:View, user: User):
        return (request.user.id == user.id or request.user.is_authenticated and request.user.is_superuser)