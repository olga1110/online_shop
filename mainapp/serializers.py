from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'category',
            'image', 'short_desc', 'desc',
            'price', 'discount', 'quantity',
            'is_active', 'modified', 'created',
        )

    def get_image(self, obj):
        return obj.image.value.url

    def get_category(self, obj):
        return obj.category.name


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name',
            'short_desc', 'desc',
            'is_active', 'modified', 'created',
        )

