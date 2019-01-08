from django import forms


# Проверка, что кол-во = целое число
def quantity_check(value):
    if value < 0:
        raise forms.ValidationError('Задано отрицательное число товаров: ', value)
    elif value == 0:
        raise forms.ValidationError('Число товаров не может быть нулевым', value)




class CartForm(forms.Form):
    quantity = forms.IntegerField(initial=1, required=False,
                                  label='количество', validators=[quantity_check]
        # widget=forms.widgets.TextInput(attrs={'class': 'form-control'} <input type=number>
        )

