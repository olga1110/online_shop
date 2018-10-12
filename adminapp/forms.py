from django import forms
from userapp.models import ShopUser
from userapp.forms import ShopUserEditForm


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'
