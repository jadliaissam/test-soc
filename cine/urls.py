from rest_framework.routers import DefaultRouter

from cine.views import MovieViewSet, ActorViewSet, ReviewViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('actors', ActorViewSet, basename='actors')
router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.get_urls()
