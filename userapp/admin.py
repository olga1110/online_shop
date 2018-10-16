from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import ShopUser


class AccountAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {
            'fields': ('avatar', 'phone')
        },
         ),
    )

admin.site.register(ShopUser, AccountAdmin)