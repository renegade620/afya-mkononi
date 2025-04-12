# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from .chatbot import PregnancyChatbot
# from .models import UserInteraction

# # Initialize the chatbot
# chatbot = PregnancyChatbot()


# def chatbot_response(request):
#     if request.method == "POST":
#         user_input = request.POST.get("message")
#         if not user_input:
#             return JsonResponse({"error": "Message is required"}, status=400)

#         response = chatbot.get_response(user_input)
#         # Log the interaction
#         UserInteraction.objects.create(
#             chatbot=None,  # Update if you have multiple chatbots
#             user_input=user_input,
#             bot_response=response,
#         )
#         return JsonResponse({"response": response})

#     return JsonResponse({"error": "Invalid request"}, status=400)


# def index(request):
#     return HttpResponse("Welcome to the Chatbot app!")


# def chat(request, session_id):
#     return HttpResponse(f"Chat session: {session_id}")


# def chatbot_interaction(request):
#     response = None
#     if request.method == "POST":
#         user_input = request.POST.get("message")
#         if user_input:
#             response = chatbot.get_response(user_input)
#             # Log the interaction
#             UserInteraction.objects.create(
#                 chatbot=None,  # Update if you have multiple chatbots
#                 user_input=user_input,
#                 bot_response=response,
#             )
#     return render(request, "chatbot_interaction.html", {"response": response})




# apps/chatbot/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .chatbot import PregnancyChatbot
from django.urls import reverse
from .models import UserInteraction, Chatbot

# Initialize the chatbot
chatbot = PregnancyChatbot()

def index(request):
    redirect_url = reverse('chatbot_interaction')
    html = f"""
    <html>
        <head>
            <meta http-equiv="refresh" content="3; url={redirect_url}" />
        </head>
        <body>
            <h2>Welcome to the Chatbot app!</h2>
            <p>You will be redirected to the chatbot in a few seconds...</p>
        </body>
    </html>
    """
    return HttpResponse(html)

def chat(request, session_id):
    return HttpResponse(f"Chat session: {session_id}")

def chatbot_interaction(request):
    # Create or get chatbot instance
    chatbot_instance, _ = Chatbot.objects.get_or_create(name="Pregnancy Bot")

    if "history" not in request.session:
        request.session["history"] = []

    response = None
    if request.method == "POST":
        user_input = request.POST.get("message")
        if user_input:
            response = chatbot.get_response(user_input)

            # Log in session for display
            chat_pair = {"user": user_input, "bot": response}
            request.session["history"].append(chat_pair)
            request.session.modified = True

            # Log in DB
            UserInteraction.objects.create(
                chatbot=chatbot_instance,
                user_input=user_input,
                bot_response=response,
            )

    return render(request, "chatbot_interaction.html", {
        "history": request.session.get("history", []),
    })
