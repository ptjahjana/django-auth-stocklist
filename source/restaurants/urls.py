from django.urls import path

from .views import (
    list, details, create, add, add_review
)

app_name='restaurants'

urlpatterns = [
    path("", list, name="list"),
    path('<int:id>/', details, name='details'),
    path('create', create, name='create'),
    path('add', add, name='add'),
    path('review', add_review, name='add_review')
]