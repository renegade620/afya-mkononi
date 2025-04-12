from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='content_index'),
    path('<int:id>/', views.detail, name='content_detail'),
]