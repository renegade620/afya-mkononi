from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("Chatbot app root"), name='chatbot-root'),
]