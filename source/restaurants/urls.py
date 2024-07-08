from django.urls import path

from .views import (
    list, details, create_restaurant, add_review
)

app_name='restaurants'

urlpatterns = [
    path("", list, name="list"),
    path('<int:id>/', details, name='details'),
    path('create', create_restaurant.as_view(), name='create'),
    path('review', add_review, name='add_review')
]