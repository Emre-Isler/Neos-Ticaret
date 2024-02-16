from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'category', 'price', 'created_at']
    list_display_links = ['name', 'owner']
    list_filter = ['owner', 'category']
    search_fields = ['name','category__name__icontains', 'owner__username__icontains']
    list_editable = ['price']
    readonly_fields = ['owner']
    date_hierarchy = 'created_at'

class CartAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'product', 'piece', 'total_price', 'created_at']
    list_filter = ['buyer']
    readonly_fields = ['total_price']
    date_hierarchy = 'created_at'

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Cart, CartAdmin)