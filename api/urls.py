from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PictureViewSet, CityViewSet, SubAreaViewSet, PropertyTypeViewSet,
    CategoryViewSet, SubCategoryViewSet, WebsiteViewSet, LocationViewSet,
    PublisherViewSet, GalleryViewSet, ProjectViewSet
)

router = DefaultRouter()
router.register(r'pictures', PictureViewSet)
router.register(r'cities', CityViewSet)
router.register(r'sub-areas', SubAreaViewSet)
router.register(r'property-types', PropertyTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sub-categories', SubCategoryViewSet)
router.register(r'websites', WebsiteViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'galleries', GalleryViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
