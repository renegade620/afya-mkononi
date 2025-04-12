from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'teleconsultations'

urlpatterns = [
    path('doctors/<int:doctor_id>/book/', views.book_consultation, name='book_consultation'),
    path('', lambda request: HttpResponse("Teleconsultations app root"), name='teleconsultations-root'),
]