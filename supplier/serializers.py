"""This file contains serializers for supplier, contact and product models"""
from rest_framework import serializers
from supplier.models import (
    Contact, Product, Factory, RetailNetwork, IndividualEntrepreneur)
# -------------------------------------------------------------------------


class ContactSerializer(serializers.ModelSerializer):
    """The ContactSerializer is a serializer for Contact models"""
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """The ProductSerializer is a serializer for Product models"""
    class Meta:
        model = Product
        fields = '__all__'


class BaseSupplierCreateSerializer(serializers.ModelSerializer):
    """This serializer is a base class for another supplier create
    serializers"""
    debt = serializers.FloatField(read_only=True)


class BaseSupplierSerializer(BaseSupplierCreateSerializer):
    """This serializer is a base class for another supplier serializers
    except create serializers"""
    contact = ContactSerializer(many=True)
    product = ProductSerializer(many=True)


class FactoryCreateUpdateSerializer(BaseSupplierCreateSerializer):
    """This serializer serves to work with the factory models during updating
    and creating process"""
    class Meta:
        model = Factory
        exclude = ['id', 'created_at', 'contact', 'product']


class FactorySerializer(BaseSupplierSerializer):
    """This serializer serves to work with the factory models during GET
    requests"""
    class Meta:
        model = Factory
        fields = '__all__'


class RetailNetworkCreateUpdateSerializer(BaseSupplierCreateSerializer):
    """This serializer serves to work with the retail network models during
    updating and creating process"""
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=Factory.objects.all(), required=False, allow_null=True)

    class Meta:
        model = RetailNetwork
        exclude = ['id', 'created_at', 'contact', 'product']


class RetailNetworkSerializer(BaseSupplierSerializer):
    """This serializer serves to work with the retail network models during GET
    requests"""
    supplier = FactorySerializer()

    class Meta:
        model = RetailNetwork
        fields = '__all__'


class EntrepreneurCreateUpdateSerializer(BaseSupplierCreateSerializer):
    """This serializer serves to work with the entrepreneur models during
    updating and creating process"""
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=RetailNetwork.objects.all(), required=False, allow_null=True)

    class Meta:
        model = IndividualEntrepreneur
        exclude = ['id', 'created_at', 'contact', 'product']


class EntrepreneurSerializer(BaseSupplierSerializer):
    """This serializer serves to work with the entrepreneur models during GET
    requests"""
    supplier = RetailNetworkSerializer()

    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'
