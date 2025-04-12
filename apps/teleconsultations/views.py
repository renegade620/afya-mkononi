from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Removed invalid import
@login_required
def doctor_list(request):
    doctors = Doctor.objects.filter(available=True)
    return render(request, 'teleconsultations/', {'doctors': doctors})
User = get_user_model()

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