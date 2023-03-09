from django.urls import path
from . import views

urlpatterns = [
    path('<str:type>/<str:id>/', views.returnhttp, name='utility')
]


