from django.db import models

class Chatbot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserInteraction(models.Model):
    chatbot = models.ForeignKey(Chatbot, on_delete=models.CASCADE)
    user_input = models.TextField()
    bot_response = models.TextField()
    interaction_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interaction with {self.chatbot.name} at {self.interaction_time}"