from django.urls import include, path
from rest_framework import routers

from .views import SignupViewSet, APIGetToken

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'signup',
                   SignupViewSet, basename='signup')


urlpatterns = [
    path('auth/token/', APIGetToken.as_view()),
    path('auth/', include(router_v1.urls)),
]
