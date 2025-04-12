from django.shortcuts import render
from django.http import HttpResponse
from .models import Wearable

def wearable_list(request):
    wearables = Wearable.objects.all()
    return render(request, 'wearables/wearable_list.html', {'wearables': wearables})

def wearable_detail(request, pk):
    wearable = Wearable.objects.get(pk=pk)
    return render(request, 'wearables/wearable_detail.html', {'wearable': wearable})

def index(request):
    return HttpResponse("Welcome to the Wearables app!")

def device(request, device_id):
    return HttpResponse(f"Wearable device ID: {device_id}")