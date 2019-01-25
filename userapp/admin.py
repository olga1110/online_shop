from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(models.ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {
            'fields': ('avatar', 'phone')
        },
         ),
    )
