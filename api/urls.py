from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PictureViewSet, LocationViewSet, PublisherViewSet, GalleryViewSet, ProjectViewSet
)
headers = {
    "X-API-KEY": "MkkcZCGe56IfRyzf82vlLwQwGJoAm5iGhzt33va3KcY"
}
print(headers)

router = DefaultRouter()
router.register(r'pictures', PictureViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'galleries', GalleryViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
