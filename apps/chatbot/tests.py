from django.test import TestCase
from .models import Chatbot

class ChatbotModelTest(TestCase):
    def setUp(self):
        self.chatbot = Chatbot.objects.create(name="Test Chatbot", description="A chatbot for testing.")

    def test_chatbot_creation(self):
        self.assertEqual(self.chatbot.name, "Test Chatbot")
        self.assertEqual(self.chatbot.description, "A chatbot for testing.")

    def test_chatbot_str(self):
        self.assertEqual(str(self.chatbot), "Test Chatbot")