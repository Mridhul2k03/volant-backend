from django.contrib import admin
from django.utils.html import format_html
from volantapp.models import Product, Size, Color, CartItem, Order, UserCart


# Register other models
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(UserCart)

# Inline classes for managing sizes and colors in Product admin
class SizeInline(admin.TabularInline):
    model = Size  # Correct this to `Size`
    extra = 1

class ColorInline(admin.TabularInline):
    model = Color  # Correct this to `Color`
    extra = 1

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview', 'available')
    search_fields = ('name', 'category')
    inlines = [SizeInline, ColorInline]  # Add inlines for size and color

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" height="100" style="object-fit: cover;"/>', obj.image.url)
        return "No Image"
    
    image_preview.short_description = 'Image Preview'

# Color Admin
class ColorAdmin(admin.ModelAdmin):
    search_fields = ('product__name', 'color')
    list_display = ('get_product_name', 'get_product_category', 'get_product_price', 'image_preview')

    def get_product_name(self, obj):
        return obj.product.name
    get_product_name.short_description = 'Product Name'

    def get_product_category(self, obj):
        return obj.product.category
    get_product_category.short_description = 'Product Category'

    def get_product_price(self, obj):
        return obj.product.price
    get_product_price.short_description = 'Product Price'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" height="100" style="object-fit: cover;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

admin.site.register(Color, ColorAdmin)

# Size Admin
class SizeAdmin(admin.ModelAdmin):
    search_fields = ('product__name', 'size')

admin.site.register(Size, SizeAdmin)
