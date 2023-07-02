from django.urls import path 
from . import views 


urlpatterns = [
    path('activate/<uidb64>/<token>/', views.activate_token, name='activate'),
    path('verify/', views.loadSuccessPage, name='success'),
    path('signup/', views.loadSignUpPage, name='signup'),
    path('login/', views.loadLoginPage, name='login'),
]