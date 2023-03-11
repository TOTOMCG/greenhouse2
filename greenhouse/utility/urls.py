from django.urls import path
from . import views

urlpatterns = [
    path('value/<str:type>/<str:id>/', views.returnvalue),
    path('chart/<str:type>/', views.returnchart)
]


