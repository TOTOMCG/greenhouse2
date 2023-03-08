from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', RedirectView.as_view(url='/main', permanent=True)),
    path('main/', include('main.urls')),
]

# urlpatterns += [
#     path('jsons/', include('jsons.urls') )
# ]
#
# setting
# urlpatterns += [
#     path('settings/', include('settings.urls')),
#     path('config/', RedirectView.as_view(url='/settings/', permanent=True)),
#     path('setting/', RedirectView.as_view(url='/settings/', permanent=True))
# ]
#
# # database
# urlpatterns += [
#     path('database/', include('database.urls')),
#     path('databases/', RedirectView.as_view(url='/database/', permanent=True)),
#     path('db/', RedirectView.as_view(url='/database/', permanent=True))
# ]
