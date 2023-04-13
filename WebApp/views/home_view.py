
from django.shortcuts import render

ROOT_URI = ''

def show(request):
    context = {}
    return render(request, 'home.html', context)
