from django.urls import path
from . import views
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.returnmain, name='main'),
]
urlpatterns += [
    path('main/', views.returnpanel, name='main'),
]


