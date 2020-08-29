from django.contrib import admin
from .models import (Category, Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # automatically pre-populates the slug field using the category name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']  # fields to be shown on the admin page
    list_filter = ['available', 'created', 'updated']  # shows a filter section on the right side of admin page
    list_editable = ['price', 'available']  # makes fields editable(changeable)
    prepopulated_fields = {'slug': ('name',)}  # automatically pre-populates the slug field using the product name
