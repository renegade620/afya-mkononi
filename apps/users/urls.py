from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users_index'),
    path('<int:id>/', views.profile, name='user_profile'),
]