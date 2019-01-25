from django import forms

from mainapp.models import Category, Product
from images.models import Image


class CategoryForm(forms.Form):
    name = forms.CharField(
        label='name',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})

    )
    short_desc = forms.CharField(label='short_desc', required=False)
    desc = forms.CharField(label='desc', required=False, widget=forms.widgets.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Подробное описание'}
        )
                           )


class ProductForm(forms.Form):
    name = forms.CharField(
        label='name',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all()
    )

    image = forms.ModelChoiceField(
        queryset=Image.objects.all()
    )

    short_desc = forms.CharField(label='short_desc', required=False)

    desc = forms.CharField(label='desc',
                           required=False,
                           widget=forms.widgets.Textarea(attrs={'class': 'form-control'}
                                                         )
                           )

    price = forms.DecimalField(
        label='price',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control'}
        )
    )

    discount = forms.DecimalField(
        label='discount',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
    quantity = forms.IntegerField(
        label='quantity',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={'class': 'form-control'}
        )
    )


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'short_desc', 'desc', 'price', 'discount', 'quantity']
        labels = {
            'category': 'Категория:',
            'image': 'Изображение'
        }
        help_texts = {
            'category': 'Выберите из списка:',
        }
        widgets = {'desc': forms.Textarea(attrs={'rows': 10, 'cols': 40})}

    # def __init__(self, *args, **kwargs):
    #     super(ProductModelForm, self).__init__(*args, **kwargs)
    # self.fields['name'].error_messages = {'required': 'Укажите название товара',
    #                                       'max_length': 'Название поле не должно превышать 150 символов'}


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'short_desc', 'desc']
