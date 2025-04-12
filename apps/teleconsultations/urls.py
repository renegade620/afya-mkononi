from django.urls import path
from . import views

app_name = 'teleconsultations'

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/book/', views.book_consultation, name='book_consultation'),
    path('teleconsultations/<int:consultation_id>/', views.consultation_detail, name='consultation_detail'),
    path('my-teleconsultations/', views.my_teleconsultations, name='my_teleconsultations'),
    path('doctors/<int:doctor_id>/available-slots/<str:date>/', views.get_available_slots, name='available_slots'),
    path('teleconsultations/<int:consultation_id>/cancel/', views.cancel_consultation, name='cancel_consultation'),
]