from django.contrib import admin
from basketapp.models import Basket


class BasketAdmin(admin.ModelAdmin):

    list_display = [
        'user', 'product', 'quantity', 'add_datetime',
    ]

    list_filter = [
        'user', 'product', 'add_datetime',

    ]

    search_fields = [
        'user', 'product',
    ]

    # def user_name(self, obj):
    #     return obj.user.username
    #
    # def product_name(self, obj):
    #     return obj.product.name


admin.site.register(Basket, BasketAdmin)

