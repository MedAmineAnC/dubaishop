from django.contrib import admin

from .models import Category, Product, HomeSlides

# Categories
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

#Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'slug', 'price', 'available', 'is_best_seller', 'is_on_sale', 'sale_price']
    list_filter = ['category', 'available', 'is_on_sale']
    list_editable = ['price', 'available', 'is_best_seller', 'is_on_sale', 'sale_price']
    prepopulated_fields = {'slug': ('name',)}

#HomeSlides
@admin.register(HomeSlides)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}