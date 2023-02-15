from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# default

# main
urlpatterns = [
    path('main/', include('main.urls')),
    path('', RedirectView.as_view(url='/main/', permanent=True)),
    path('main/humidity', include('humidity.urls')),
    path('main/temperature', include('temperature.urls')),
    path('main/watering', include('watering.urls')),
    path('main/window', include('window.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# setting
urlpatterns += [
    path('settings/', include('settings.urls')),
    path('config/', RedirectView.as_view(url='/settings/', permanent=True)),
    path('setting/', RedirectView.as_view(url='/settings/', permanent=True))
]

# database 
urlpatterns += [
    path('database/', include('database.urls')),
    path('databases/', RedirectView.as_view(url='/database/', permanent=True)),
    path('db/', RedirectView.as_view(url='/database/', permanent=True))
]

urlpatterns += [
    path('main/window/', include('window.urls')),
    path('main/windows/', RedirectView.as_view(url='/main/window', permanent=True))
]

urlpatterns += [
    path('main/temperature/', include('temperature.urls'))
]

urlpatterns += [
    path('main/humidity/', include('humidity.urls'))
]

urlpatterns += [
    path('main/watering/', include('watering.urls'))
]