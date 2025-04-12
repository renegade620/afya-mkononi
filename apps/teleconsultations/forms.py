from django import forms
from django.db import models
from django.utils import timezone
from datetime import date, timedelta

class Consultation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['doctor', 'date', 'start_time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'reason': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("You cannot book a consultation in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        doctor = cleaned_data.get('doctor')

        if date and start_time and doctor:
            # Check if doctor is available at this time
            consultation_datetime = timezone.make_aware(
                timezone.datetime.combine(date, start_time)
            )
            end_datetime = consultation_datetime + timedelta(minutes=30)
            
            conflicting_teleconsultations = Consultation.objects.filter(
                doctor=doctor,
                date=date,
                start_time__lt=end_datetime.time(),
                end_time__gt=start_time,
                status__in=['confirmed', 'pending']
            ).exclude(pk=self.instance.pk if self.instance else None)

            if conflicting_teleconsultations.exists():
                raise forms.ValidationError("The doctor is not available at this time. Please choose another time slot.")