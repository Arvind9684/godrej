from rest_framework import viewsets,status
from .models import (
    Picture,City, SubArea, PropertyType, Category, SubCategory, Website,
    Location, Publisher, Gallery, Project
)
from .serializers import (
    PictureSerializer, CitySerializer, SubAreaSerializer, PropertyTypeSerializer,
    CategorySerializer, SubCategorySerializer, WebsiteSerializer, LocationSerializer,
    PublisherSerializer, GallerySerializer, ProjectSerializer,UserSerializer
)
from api.authentication import APIKeyAuthentication
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsSpecificSuperuser


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsSpecificSuperuser]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsSpecificSuperuser]

class SubAreaViewSet(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    permission_classes = [IsAuthenticated]

class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = [IsAuthenticated]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAuthenticated]

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [IsSpecificSuperuser]
