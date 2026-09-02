from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),

    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]






# from django.contrib import admin
# from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path('', include('core.urls') ),
#     # path('shop/', shop, name='shop'),
#     path('cart/', include('cart.urls')),

#     path('items/', include('item.urls')),
#     path('admin/', admin.site.urls),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

