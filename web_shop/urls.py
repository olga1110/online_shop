from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import mainapp.urls.products as products
import mainapp.urls.categories as categories
import userapp.urls as userapp
import adminapp.urls as adminapp
import basketapp.urls as basketapp


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include(adminapp)),
    path('', include(products)),
    path('catalog/', include(categories)),
    path('auth/', include(userapp)),
    path('basket/', include(basketapp)),
    # url(r'^catalog/', include(('mainapp.urls', 'catalog'), namespace='catalog')),
    # url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

