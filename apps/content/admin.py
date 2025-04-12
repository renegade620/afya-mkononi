from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient__username', 'doctor__username')

# filepath: c:\AFYAMKONONI3\Afya\apps\teleteleconsultations\apps.py
from django.apps import AppConfig

