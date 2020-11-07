from django.contrib import admin
from .models import Category, Position, Order

admin.site.register(Category)


@admin.register(Position)
class GpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price')
    list_filter = ('id', 'category', 'name', 'price')


@admin.register(Order)
class GpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'time', 'position_id', 'price')
    list_filter = ('time', 'seller', 'position_id', 'price')

