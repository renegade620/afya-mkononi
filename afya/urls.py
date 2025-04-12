from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# View for the landing page
def landing_page(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),  # Root URL for the landing page
    path('chatbot/', include('apps.chatbot.urls')),
    path('content/', include('apps.content.urls')),
    path('users/', include('apps.users.urls')),
    path('teleconsultations/', include('apps.teleconsultations.urls')),  # Corrected path
]