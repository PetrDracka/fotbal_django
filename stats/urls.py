from django.urls import path
from . import views

urlpatterns = [
    path('', views.vypis_hracu, name='vypis_hracu'),
]