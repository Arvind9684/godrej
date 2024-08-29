from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Removed name='admin'
    path('', include('myapp.urls'), name='index'),  # Include myapp urls
    path('api/', include('api.urls')),  # Include api urls
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # API authentication
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)