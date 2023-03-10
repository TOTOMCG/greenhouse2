from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', RedirectView.as_view(url='/main', permanent=True)),
    path('main/', include('main.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
  path('utility/', include('utility.urls'))
]

handler404 = "greenhouse.views.page_not_found_view"