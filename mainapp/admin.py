from django.contrib import admin
from django.template.loader import render_to_string
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category_name', 'picture', 'short_desc',
        'price', 'is_active', 'modified', 'created',
    ]

    list_filter = [
        'category', 'image', 'is_active',
        'modified', 'created',
    ]

    search_fields = [
        'name', 'desc', 'short_desc',
    ]

    def picture(self, obj):
        return render_to_string(
            'mainapp/components/picture.html',
            {'image': obj.image.value.url}
        )

    def category_name(self, obj):
        return obj.category.name.title()

    fieldsets = (
        (
            'Title', {
                'fields': ('name', 'category')
            },
        ),
        (
            'Content', {
                'fields': ('image', 'short_desc', 'discount', 'quantity', 'desc')
            },
        ),
    )


class ProductInline(admin.TabularInline):
    model = Product
    fk_name = 'category'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'short_desc', 'is_active',
        'modified', 'created',
    ]

    list_filter = [
        'is_active',
        'modified', 'created',
    ]

    search_fields = [
        'name', 'desc', 'short_desc',
    ]

    inlines = [
        ProductInline
    ]

# admin.site.register(models.Product, ProductAdmin)
# admin.site.register(Category)
