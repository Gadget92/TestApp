from django.contrib import admin

from .models import Product, Filial, FilialPrice, Characteristic

admin.site.register(Product)
admin.site.register(Filial)
admin.site.register(FilialPrice)
admin.site.register(Characteristic)
