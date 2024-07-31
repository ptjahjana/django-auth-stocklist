from django.contrib import admin

from .models import Stock, Fabric, Color

admin.site.register(Fabric)
admin.site.register(Color)
admin.site.register(Stock)