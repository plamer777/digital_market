"""This file contains ViewSets to render different entities"""
from typing import Type
from django.db.models.manager import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from supplier.models import Factory, IndividualEntrepreneur, RetailNetwork
from supplier import serializers
from supplier.permissions import IsStaffPermission
from supplier import filters
# --------------------------------------------------------------------------


class BaseViewSet(ModelViewSet):
    """The BaseViewSet used to be inherited by another viewsets. The viewset
    provides necessary permissions and additional functionality"""
    permission_classes = [IsAuthenticated, IsStaffPermission]
    filter_backends = [DjangoFilterBackend]

    def get_supplier_object(
            self) -> Factory | IndividualEntrepreneur | RetailNetwork | None:
        """This additional method serves to get instance of necessary
        supplier
        :return: instance depending on the used route on None if route is not
        recognized
        """
        pk = self.kwargs.get('id_pk')
        route = str(self.request.parser_context['request'])

        if 'entrepreneur' in route:
            result = IndividualEntrepreneur.objects.filter(
                pk=pk).first()

        elif 'retail_network' in route:
            result = RetailNetwork.objects.filter(
                pk=pk).first()

        elif 'factory' in route:
            result = Factory.objects.filter(pk=pk).first()

        else:
            result = None

        return result


class ContactViewSet(BaseViewSet):
    """This viewset serves to render Contact entities"""
    serializer_class = serializers.ContactSerializer

    def get_queryset(self) -> QuerySet | None:
        """This method was rewritten to get Contact entities for certain
        supplier model
        :return: a queryset of Contact entities or None if no entities
        """
        result = self.get_supplier_object()
        return result.contact.all() if result else None

    def perform_create(
            self, serializer: serializers.ContactSerializer) -> None:
        """This method has been rewritten so that the created model was added
        to the parent model it was created for"""
        parent_instance = self.get_supplier_object()
        new_contact = serializer.save()
        parent_instance.contact.add(new_contact)


class ProductViewSet(BaseViewSet):
    """This viewset serves to render Product entities"""
    serializer_class = serializers.ProductSerializer

    def get_queryset(self) -> QuerySet | None:
        """This method was rewritten to get Product entities for certain
        supplier model
        :return: a queryset of Product entities or None if no entities
        """
        result = self.get_supplier_object()
        return result.product.all() if result else None

    def perform_create(
            self, serializer: serializers.ProductSerializer) -> None:
        """This method has been rewritten so that the created model was added
        to the parent model it was created for"""
        parent_instance = self.get_supplier_object()
        new_product = serializer.save()
        parent_instance.product.add(new_product)


class FactoryViewSet(BaseViewSet):
    """This viewset serves to render Factory entities"""
    queryset = Factory.objects.all()
    filterset_class = filters.CityFilter
    _serializers = {
        'list': serializers.FactorySerializer,
        'retrieve': serializers.FactorySerializer,
        'destroy': serializers.FactorySerializer,
        'create': serializers.FactoryCreateUpdateSerializer,
        'update': serializers.FactoryCreateUpdateSerializer,
        'partial_update': serializers.FactoryCreateUpdateSerializer,
    }
    default_serializer = serializers.FactorySerializer

    def get_serializer_class(
            self) -> Type[
        serializers.FactorySerializer |
        serializers.FactoryCreateUpdateSerializer |
        serializers.FactoryCreateUpdateSerializer
        ]:
        """This method serves to get the serializer class for current action
        :return: the serializer class
        """
        serializer = self._serializers.get(
            self.action, self.default_serializer)

        return serializer


class RetailNetworkViewSet(BaseViewSet):
    """This viewset serves to render RetailNetwork entities"""
    queryset = RetailNetwork.objects.all()
    filterset_class = filters.CityFilter
    _serializers = {
        'list': serializers.RetailNetworkSerializer,
        'retrieve': serializers.RetailNetworkSerializer,
        'destroy': serializers.RetailNetworkSerializer,
        'create': serializers.RetailNetworkCreateUpdateSerializer,
        'update': serializers.RetailNetworkCreateUpdateSerializer,
        'partial_update': serializers.RetailNetworkCreateUpdateSerializer,
    }
    default_serializer = serializers.RetailNetworkSerializer

    def get_serializer_class(
            self) -> Type[
        serializers.RetailNetworkSerializer |
        serializers.RetailNetworkCreateUpdateSerializer |
        serializers.RetailNetworkCreateUpdateSerializer
        ]:
        """This method serves to get the serializer class for current action
        :return: the serializer class
        """
        serializer = self._serializers.get(
            self.action, self.default_serializer)

        return serializer


class EntrepreneurViewSet(BaseViewSet):
    """This viewset serves to render RetailNetwork entities"""
    queryset = IndividualEntrepreneur.objects.all()
    filterset_class = filters.CityFilter
    _serializers = {
        'list': serializers.EntrepreneurSerializer,
        'retrieve': serializers.EntrepreneurSerializer,
        'destroy': serializers.EntrepreneurSerializer,
        'create': serializers.EntrepreneurCreateUpdateSerializer,
        'update': serializers.EntrepreneurCreateUpdateSerializer,
        'partial_update':
            serializers.EntrepreneurCreateUpdateSerializer,
    }
    default_serializer = serializers.EntrepreneurSerializer

    def get_serializer_class(
            self) -> Type[
        serializers.EntrepreneurSerializer |
        serializers.EntrepreneurCreateUpdateSerializer |
        serializers.EntrepreneurCreateUpdateSerializer
        ]:
        """This method serves to get the serializer class for current action
        :return: the serializer class
        """
        serializer = self._serializers.get(
            self.action, self.default_serializer)

        return serializer
