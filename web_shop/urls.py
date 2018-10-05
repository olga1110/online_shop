from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
import mainapp.urls.products as products
import mainapp.urls.categories as categories
import userapp.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(products)),
    path('',include(categories)),
    # path(r'^auth/', include('userapp.urls')),
    # url(r'^catalog/', include(('mainapp.urls', 'catalog'), namespace='catalog')),
    # url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

