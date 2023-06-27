from django.urls import path 
from . import views 


urlpatterns = [
    path('account-settings/', views.loadDashboard, name='dashboard')
]