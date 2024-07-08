from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class CreateRestaurantForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=50, required=True)
    street_address = forms.CharField(label=_('Street Address'), max_length=50, required=False)
    description = forms.CharField(label=_('Description'), max_length=150, required=False)
