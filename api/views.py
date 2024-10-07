from rest_framework import viewsets,status
from .models import (
    Picture, Location, Publisher, Gallery, Project
)
from .serializers import (
    PictureSerializer, LocationSerializer,
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
