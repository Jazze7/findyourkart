
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls", namespace='users')),
    path('', include("web.urls", namespace='web')),
    path('products/', include("products.urls", namespace='products')),
]
if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)


    )