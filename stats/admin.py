from django.contrib import admin
from .models import Hrac

# Registrujeme pouze model Hrac, protože ostatní jsme smazali
admin.site.register(Hrac)