from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    list_display = ('name', 'parent', 'slug')
    search_fields = ('name',)


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    inlines = [ImageInline]
    list_display = ('name', 'category', 'created_at', 'slug',)
    search_fields = ('name',)
    list_filter = ('category', 'created_at')


class ProductImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductImage

    list_display = ('product',)
    list_filter = ('created_at',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Size)
