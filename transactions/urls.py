from django.urls import path 
from . import views



urlpatterns = [
    path('transfer/', views.loadTransferPage, name='transfer')
]