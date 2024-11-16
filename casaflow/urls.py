from django.contrib import admin
from django.urls import path, include  # Import include to reference app-specific urls.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('casa.urls')),  # Directs root URL traffic to the `casaflow` app's urls.py
]