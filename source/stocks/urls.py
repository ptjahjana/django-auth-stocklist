from django.urls import path

from .views import (
    list,
)

app_name='stocks'

urlpatterns = [
    path("", list, name="list"),
]