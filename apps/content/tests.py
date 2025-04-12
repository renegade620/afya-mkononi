from django.test import TestCase
from .models import Content

class ContentModelTest(TestCase):

    def setUp(self):
        Content.objects.create(title="Test Content", body="This is a test content body.")

    def test_content_creation(self):
        content = Content.objects.get(title="Test Content")
        self.assertEqual(content.body, "This is a test content body.")