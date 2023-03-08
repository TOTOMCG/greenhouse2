from django.urls import path
from . import views

urlpatterns = [
    path('', views.returnjson, name='utility'),
]


