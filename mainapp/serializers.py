from rest_framework import serializers

from mainapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'category', 'image',
            'short_desc', 'desc', 'price',
            'discount', 'quantity', 'modified', 'created',
        )

