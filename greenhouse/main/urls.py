from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static 

# влажность 
urlpatterns = [
    path('', views.returnmain, name='main'),
]


