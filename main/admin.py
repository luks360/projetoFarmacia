from django.contrib import admin
from main.models import Client, Medicament, Pharmacy, Request

# Register your models here.

admin.site.register(Client)
admin.site.register(Medicament)
admin.site.register(Pharmacy)
admin.site.register(Request)