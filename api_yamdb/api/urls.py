from django.urls import include, path
from rest_framework import routers

from .views import SignupViewSet, APIGetToken, UsersViewSet, current_user

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'auth/signup',
                   SignupViewSet, basename='signup')
router_v1.register(r'users',
                   UsersViewSet, basename='users')


urlpatterns = [
    path('auth/token/', APIGetToken.as_view()),
    path('users/me/', current_user),
    path('', include(router_v1.urls)),
]
