"""This file contains routers for supplier viewsets"""
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter
from supplier import views
# --------------------------------------------------------------------------

router = SimpleRouter()

router.register('factory', viewset=views.FactoryViewSet)
factory_router = NestedSimpleRouter(router, 'factory', lookup='id')
factory_router.register('contact', views.ContactViewSet, basename='contact')
factory_router.register('product', views.ProductViewSet, basename='product')

router.register('retail_network', viewset=views.RetailNetworkViewSet)
retail_router = NestedSimpleRouter(router, 'retail_network', lookup='id')
retail_router.register('contact', views.ContactViewSet, basename='contact')
retail_router.register('product', views.ProductViewSet, basename='product')

router.register('entrepreneur', viewset=views.EntrepreneurViewSet)
entrepreneur_router = NestedSimpleRouter(router, 'entrepreneur', lookup='id')
entrepreneur_router.register(
    'contact', views.ContactViewSet, basename='contact')
entrepreneur_router.register(
    'product', views.ProductViewSet, basename='product')
