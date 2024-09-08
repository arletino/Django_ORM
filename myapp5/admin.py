from django.contrib import admin
from .models import Category, Product


@admin.action(description='Reset quantity to zero')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    '''List of product'''
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Search by field description (description)'
    actions = [reset_quantity]

    '''Other product'''
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Additional',
            {
                'classes': ['collapse'],
                'description': 'Category of product and description of product',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Economical',
            {
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'Rating and other staff',
            {
                'description': 'Rating auto generated on clients marks',
                'fields': ['rating', 'date_added'],
            },
        ),



    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

# Register your models here.

