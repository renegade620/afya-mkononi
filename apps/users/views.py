from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    return HttpResponse("List of users")

def user_detail(request, user_id):
    return HttpResponse(f"Details of user {user_id}")

def user_create(request):
    return HttpResponse("Create a new user")

def user_update(request, user_id):
    return HttpResponse(f"Update user {user_id}")

def user_delete(request, user_id):
    return HttpResponse(f"Delete user {user_id}")

def index(request):
    return HttpResponse("Welcome to the Users app!")

def profile(request, id):
    return HttpResponse(f"User profile for ID: {id}")