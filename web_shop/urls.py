from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

import mainapp.urls.products as products
import mainapp.urls.categories as categories
import userapp.urls as userapp
import basketapp.urls as basketapp
import adminapp.urls as adminapp
from mainapp.endpoints.products import ProductViewSet
from mainapp.endpoints.category import CategoryViewSet, category_list, category_detail
from basketapp.endpoints.basket import BasketViewSet
from userapp.endpoints.shop_user import ShopUserViewSet

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('basket', BasketViewSet)
router.register('users', ShopUserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_custom/', include(adminapp)),
    path('', include(products)),
    path('catalog/', include(categories)),
    path('auth/', include(userapp)),
    path('basket/', include(basketapp)),
    path('api/', include(router.urls)),
    path('schema/', schema_view),
    # path('pages/', include('django.contrib.flatpages.urls'),
    # url(r'^catalog/', include(('mainapp.urls', 'catalog'), namespace='catalog')),
    # url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
