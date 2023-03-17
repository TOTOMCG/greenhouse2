from django.urls import path
from . import views

urlpatterns = [
    path('values/<str:type>/<str:id>/', views.returnvalue),
    path('charts/<str:type>/', views.returnchart),
    path('table/', views.returntable)
]


