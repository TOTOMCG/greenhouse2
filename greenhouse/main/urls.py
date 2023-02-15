from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.returnmain, name='main/temperature.html'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# влажность 
urlpatterns += [
    path('humidity/', views.returnmainhumidity, name='humidity/humidity.html')
]

# температура 
urlpatterns += [
    path('temperature/', views.returnmaintemperature, name='temperature/temperature.html')
]