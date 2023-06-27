from django.shortcuts import render, redirect 
from customers_app.models import Users, Customers
from django.contrib.auth import logout


def loadDashboard(request):
    print(request.user)
    context = {
        'current_user': request.user,
        }
    return render(request, 'dash/dash.html', context)


def logout(request):
    return 
