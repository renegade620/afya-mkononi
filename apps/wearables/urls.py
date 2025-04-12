from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='wearables_index'),
    path('<int:device_id>/', views.device, name='wearables_device'),
]