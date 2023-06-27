from django.shortcuts import render
from django.http import HttpResponse


def loadIndexPage(request):
    return render(request, 'index/pages/index.html')
