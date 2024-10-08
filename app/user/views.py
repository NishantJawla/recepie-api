"""
Views for the user app
"""

from rest_framework import generics, authentication, permissions
from user.serializers import (UserSerializer, AuthTokenSerializer,)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class CreateUserView(generics.CreateAPIView):
    """
    API view for creating a new user in the system
    """

    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """
    API view for creating a new auth token for the user
    """

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    API view for managing the authenticated user
    """

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """
        Retrieve and return the authenticated user
        """
        return self.request.user
    