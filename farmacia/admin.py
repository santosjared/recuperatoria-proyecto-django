from django.contrib import admin
from .models import Medicament
from .models import Client

admin.site.register(Medicament)
admin.site.register(Client)

# Register your models here.
