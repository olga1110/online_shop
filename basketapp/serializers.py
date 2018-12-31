from rest_framework import serializers

from .models import Basket


class BasketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Basket
        fields = (
            'id', 'user', 'product',
            'quantity', 'add_datetime'
        )
