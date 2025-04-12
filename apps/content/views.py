from django.shortcuts import render
from .models import Content
from django.http import HttpResponse

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content/content_list.html', {'contents': contents})

def content_detail(request, pk):
    content = Content.objects.get(pk=pk)
    return render(request, 'content/content_detail.html', {'content': content})

def index(request):
    return HttpResponse("Welcome to the Content app!")

def detail(request, id):
    return HttpResponse(f"Content detail for ID: {id}")