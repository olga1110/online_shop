import rest_framework.viewsets as viewsets

from basketapp.serializers import BasketSerializer
from basketapp.models import Basket


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all().order_by('user', 'product')
    serializer_class = BasketSerializer