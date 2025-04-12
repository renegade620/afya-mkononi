from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Consultation(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teleconsultations_as_patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teleconsultations_as_doctor')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')

    def __str__(self):
        return f"Consultation with {self.doctor} on {self.date} at {self.start_time}"

class teleteleconsultations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation_date = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f"Consultation for {self.user.username} on {self.consultation_date}"

class Chatbot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chatbot interaction with {self.user.username}"

class Wearable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_name