from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static 

# влажность 
urlpatterns = [
    path('', RedirectView.as_view(url='/main/humidity/', permanent=True)),
    path('humidity/', views.returnmainhumidity, name='humidity/humidity.html'),
    path('temperature/', views.returnmaintemperature, name='temperature/temperature.html')
]


