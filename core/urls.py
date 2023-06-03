"""This file contains urls to process user's routes"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView)
from core.views import UserCreateView
# -------------------------------------------------------------------------

urlpatterns = [
    path('signup/', UserCreateView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
