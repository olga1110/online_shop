from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import mainapp.urls.products as products
import mainapp.urls.categories as categories
import userapp.urls as userapp
import basketapp.urls as basketapp
import adminapp.urls as adminapp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_custom/', include(adminapp)),
    path('', include(products)),
    path('catalog/', include(categories)),
    path('auth/', include(userapp)),
    path('basket/', include(basketapp)),
    # path('pages/', include('django.contrib.flatpages.urls'),
    # url(r'^catalog/', include(('mainapp.urls', 'catalog'), namespace='catalog')),
    # url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

