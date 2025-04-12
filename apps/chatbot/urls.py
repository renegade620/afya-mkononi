from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chatbot_index'),
    path('chat/<str:session_id>/', views.chat, name='chatbot_chat'),
]