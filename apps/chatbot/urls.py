# from django.urls import path
# from .views import chatbot_response, index, chatbot_interaction

# urlpatterns = [
#     path("", index, name="index"),  # Root URL for the index page
#     path("chatbot/", chatbot_interaction, name="chatbot-interaction"),  # Updated
#     path("api/", chatbot_response, name="chatbot-api"),
# ]



# apps/chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("interact/", views.chatbot_interaction, name="chatbot_interaction"),
]
