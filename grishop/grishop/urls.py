from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)