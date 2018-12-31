import rest_framework.viewsets as viewsets

from userapp.serializers import ShopUserSerializer
from userapp.models import ShopUser


class ShopUserViewSet(viewsets.ModelViewSet):
    queryset = ShopUser.objects.all().order_by('is_superuser')
    serializer_class = ShopUserSerializer