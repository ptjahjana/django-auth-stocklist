import django_filters
from django import forms
from .models import Stock, Fabric, Color

class StockFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = {
            'fabric': ['exact'],
            'color': ['exact'],
        }