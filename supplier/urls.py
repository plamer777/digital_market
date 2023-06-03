"""This file contains urls for supplier viewsets"""
from django.urls import path, include
from supplier import routers
# --------------------------------------------------------------------------

urlpatterns = [
    path('', include(routers.router.urls)),
    path('', include(routers.factory_router.urls)),
    path('', include(routers.retail_router.urls)),
    path('', include(routers.entrepreneur_router.urls)),
]
