from django.contrib import admin
from .models import Product, Category, InventoryItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(InventoryItem)