from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    pass
