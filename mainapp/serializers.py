from rest_framework import serializers

from mainapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = (
            'id', 'name', 'category', 'image',
            'short_desc', 'desc', 'price',
            'discount', 'quantity', 'modified', 'created',
        )

    def get_image(self, obj):
        return obj.image.value.url

    def get_category(self, obj):
        return obj.category.name


class Person(object):
    pass






