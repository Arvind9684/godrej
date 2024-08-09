# api/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from .models import APIKey

class APITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password123')
        self.api_key = APIKey.objects.create(user=self.user)

    def test_register_user(self):
        url = reverse('register-user')
        data = {
            "username": "Arvind",
            "email": "arvindgzp672@gmail.com",
            "password": "Arvind@123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_api_key(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('get-api-key')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['api_key'], self.api_key.key)

    def test_protected_view(self):
        url = reverse('protected-view')
        self.client.credentials(HTTP_X_API_KEY=self.api_key.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Add tests to your urls.py
from django.urls import path
from .views import RegisterUser, GetAPIKey, ProtectedView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('get-api-key/', GetAPIKey.as_view(), name='get-api-key'),
    path('protected/', ProtectedView.as_view(), name='protected-view'),
]
