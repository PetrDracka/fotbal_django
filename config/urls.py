from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Tady musí být .urls a ne ten znak
    path('', include('stats.urls')),
]