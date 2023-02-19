from django.urls import path
from . import views
from django.conf.urls.static import static 

# влажность 
urlpatterns = [
    path('main/', views.returnmain, name='main'),
]


