"""This file contains classes to introduce suppliers, products and contacts in
the django admin panel"""
from typing import Type
from django.forms import BaseModelForm
from django.contrib import admin, messages
from django.urls import reverse
from django.http import HttpRequest
from django.utils.safestring import mark_safe, SafeString
from django.db.models.manager import QuerySet
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Contact, \
    Product, BaseModel
# --------------------------------------------------------------------------


@admin.action(description='Обнулить долг для выбранных поставщиков')
def clear_debt(
        modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    """This action allows user with superuser role to clear the debts for
    selected suppliers using admin panel"""
    try:
        if request.user.is_superuser:
            queryset.update(debt=0.0)
        else:
            modeladmin.message_user(
                request, message=f'У вас недостаточно прав',
                level=messages.INFO)

    except Exception as e:
        modeladmin.message_user(
            request, message=f'При очистке возникла ошибка: {e}',
            level=messages.ERROR)


class BaseAdmin(admin.ModelAdmin):
    """The BaseAdmin class contains all common fields to be inherited by
    another admin classes"""
    list_display = (
        'name', 'contacts', 'products', 'debt', 'created_at')
    list_filter = ('contact__city',)
    search_fields = ('name', 'contact__city', 'contact__country')
    actions = [clear_debt]

    def get_form(
            self, request: HttpRequest, obj=None, change=False, **kwargs
    ) -> Type[BaseModelForm]:
        """This method serves to restrict to change the debt field of
        supplier models for users without superuser role"""
        form = super().get_form(request, obj, **kwargs)
        is_admin = request.user.is_superuser

        if not is_admin:
            form.base_fields['debt'].disabled = True

        return form

    @admin.display
    def contacts(self, obj: BaseModel) -> str:
        """This method serves to get all contacts for certain supplier
        :param obj: an instance of any classes inherited from BaseModel
        :return: a string containing contacts
        """
        return ', '.join(str(item) for item in obj.contact.all())

    @admin.display
    def products(self, obj: BaseModel) -> str:
        """This method serves to get all products for certain supplier
        :param obj: an instance of any classes inherited from BaseModel
        :return: a string containing products
        """
        return ', '.join(str(item) for item in obj.product.all())

    class Meta:
        abstract = True


@admin.register(Factory)
class FactoryAdmin(BaseAdmin):
    """This class represents a factory in the admin panel"""
    pass


@admin.register(RetailNetwork)
class RetailNetworkAdmin(FactoryAdmin):
    """This class represents a retail network in the admin panel"""
    list_display = (
        'name', 'contacts', 'products', 'debt', 'supplier_link', 'created_at')

    def supplier_link(
            self, obj: RetailNetwork | IndividualEntrepreneur) -> SafeString:
        """This method serves to get a link to the upper-level supplier of
        current supplier"""
        link = None
        reference = (f'admin:supplier'
                     f'_{type(obj.supplier).__name__.lower()}_change')
        if obj.supplier:
            link = mark_safe(
                '<a href={}>{}</a>'.format(
                reverse(reference, args=[obj.supplier.id]), obj.supplier.name))

        return link

    supplier_link.short_description = 'Ссылка на поставщика'


@admin.register(IndividualEntrepreneur)
class EntrepreneurAdmin(RetailNetworkAdmin):
    """This class represents an entrepreneur in the admin panel"""
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """This class represents a contact in the admin panel"""
    list_display = ('email', 'country', 'city', 'street')
    search_fields = ('email', 'city', 'country', 'street')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """This class represents a product in the admin panel"""
    list_display = ('name', 'release_date', 'model')
    search_fields = ('name', 'model')
