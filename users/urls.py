# project/urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import user_registration  # Import the user_registration view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('register/', user_registration, name='user_registration'),  # Add the registration view
]
