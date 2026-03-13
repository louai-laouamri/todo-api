from django.urls import path, include
import os

urlpatterns = [
    path('api/', include('todos.urls')),
]

SECRET_KEY=os.getenv("SECRET_KEY", "django-insecure-default-key-for-dev")
DEBUG=True