from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
    
from .views import CategoryViewSet, GenreViewSet, TitleViewSet, CommentsViewSet, ReviewViewSet

from .views import SignupViewSet, APIGetToken, UsersViewSet, current_user

router_v1 = SimpleRouter()

app_name = 'api'

router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet, basename='comments')
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
    path('v1/api-token-auth/', views.obtain_auth_token),
]
