from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

from .views import SignupViewSet, APIGetToken, UsersViewSet, current_user

router_v1 = SimpleRouter()

app_name = 'api'

router_v1.register(r'auth/signup',
                   SignupViewSet, basename='signup')
router_v1.register(r'users',
                   UsersViewSet, basename='users')

router_v1.register(
    'categories',
    CategoryViewSet,
    basename='сategories'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)

urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view()),
    path('v1/users/me/', current_user),
    path('v1/', include(router_v1.urls)),
]
