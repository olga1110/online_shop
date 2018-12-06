from django.contrib import admin
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from . import models


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'image', 'short_desc', 'price', 'modified', 'created']


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category_name', 'picture', 'short_desc',
        'price', 'modified', 'created',
    ]

    list_filter = [
        'category', 'image',
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
        # return mark_safe('''
        # <div class="image">
        #     <div class="image__value" style="background-image: url(%s)">
        #     </div>
        # </div>
        # ''' % obj.image.value.url)

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
                'fields': ('image', 'short_desc','discount', 'quantity', 'desc')
            },
        ),
    )




admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)