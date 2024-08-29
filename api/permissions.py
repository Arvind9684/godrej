# api/permissions.py
from rest_framework.permissions import BasePermission

class IsSpecificSuperuser(BasePermission):
    def has_permission(self, request, view):
        # Replace 'your_superuser_username' with the actual superuser username
        return request.user and request.user.is_superuser and request.user.username == 'Arvind'
