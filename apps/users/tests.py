from django.test import TestCase
from .models import User  # Adjust the import based on your actual User model

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')  # Adjust based on your __str__ method in User model

    def test_user_password(self):
        self.assertTrue(self.user.check_password('password123'))  # Ensure password is hashed and can be checked

    def tearDown(self):
        self.user.delete()