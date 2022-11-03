from rest_framework.views import Request, View
from rest_framework import permissions


class isAdminOrReadOnly(permissions.BasePermission):


    def has_permission(self, request: Request, view: View):


        return (request.method == "GET" or request.user.is_superuser)


