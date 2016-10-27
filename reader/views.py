from django.shortcuts import render
from .models import Countries, Regions


def index(request):
    return render(request, 'reader/index.html')


def diagram(request):
    filename = request.POST['file']
    region = request.POST['region_id']
    context = {
        'file': filename,
        'region': region
    }
    return render(request, 'reader/diagram.html', context)
