from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    bio = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"
    def __str__(self):
        return f"Consultation with {self.doctor} on {self.date} at {self.start_time}"