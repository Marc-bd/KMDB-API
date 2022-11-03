from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users import views




urlpatterns = [
    path('users/register/', views.UserViews.as_view()),
    path('users/login/', obtain_auth_token),
    path('users/', views.UserViews.as_view()),
    path('users/<int:user_id>/', views.UserDetailViews.as_view())
]
