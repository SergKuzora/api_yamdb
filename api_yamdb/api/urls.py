  
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CategoryViewSet

router_v1 = SimpleRouter()

router_v1.register(
    'Categories',
    CategoryViewSet,
    basename='сategories'
)
router_v1.register(
    'Titles',
    CategoryViewSet,
    basename='titles'
)
router_v1.register(
    'Genres',
    CategoryViewSet,
    basename='genres'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
