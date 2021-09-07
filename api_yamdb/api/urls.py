from api.views import CommentsViewSet, ReviewViewSet
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
