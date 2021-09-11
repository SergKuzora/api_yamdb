from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

from .views import SignupViewSet, APIGetToken

router_v1 = SimpleRouter()

app_name = 'api'

# router_v1 = routers.DefaultRouter()
router_v1.register(r'signup',
                   SignupViewSet, basename='signup')

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
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/auth/token/', APIGetToken.as_view()),
    path('v1/auth/', include(router_v1.urls)),
]
