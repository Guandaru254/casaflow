from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views  # Import the home view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the home page
    path("register/", views.register, name='register'), 
    path('login/', views.login, name='login'),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)