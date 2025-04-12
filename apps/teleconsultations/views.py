from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Doctor  # Import the Doctor model

@login_required
def doctor_list(request):
    doctors = Doctor.objects.filter(available=True)
    return render(request, 'teleconsultations/', {'doctors': doctors})

@login_required
def book_consultation(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    # Add logic to handle booking (e.g., saving to the database)
    return HttpResponse(f"Consultation booked with Dr. {doctor.name}")

User = get_user_model()