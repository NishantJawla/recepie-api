"""
Url module for user app
"""

from django.urls import path

from user.views import (CreateUserView, CreateTokenView, ManageUserView,)

app_name = 'user'
# app_name is used to identify the app in the url template tag and used in the reverse function to identify the app

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('me/', ManageUserView.as_view(), name='me'),
]
