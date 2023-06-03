"""This file contains filterset classes for supplier application"""
from django_filters import FilterSet
from django_filters import filters
# ---------------------------------------------------------------------------


class CityFilter(FilterSet):
    """This filter is used to filter entities by the city field of a 'contact'
    relation"""
    city = filters.CharFilter(
        field_name="contact__city", lookup_expr='icontains')
