from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls)
]

urlpatterns += [
    path('main/', include('main.urls')),
    path('', RedirectView.as_view(url='/main/', permanent=True))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('settings/', include('settings.urls')),
    path('config/', RedirectView.as_view(url='/settings/', permanent=True)),
    path('setting/', RedirectView.as_view(url='/settings/', permanent=True))
] 