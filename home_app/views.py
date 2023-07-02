from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib import messages


def loadIndexPage(request):
    print(request.user)
    context = {
        'current_user': request.user,
        }
    return render(request, 'index/pages/index.html', context)



def logoutUser(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out successfully!')
        return redirect('login')
