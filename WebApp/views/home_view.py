
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

ROOT_URI = ''

@csrf_exempt
def show(request):
    context = {}
    return render(request, 'home.html', context)
