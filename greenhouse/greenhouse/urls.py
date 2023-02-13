from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls)
]

urlpatterns += [
    path('main/', include('main.urls')),
    path('', RedirectView.as_view(url='/main/', permanent=True))
]
