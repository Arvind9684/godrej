from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey  # Assuming you have an APIKey model

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')

        if not api_key:
            return None  # No API key provided, move on to other authentication methods

        try:
            key = APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')

        return (key.user, None)  # Authentication successful
