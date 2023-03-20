from django.contrib import admin
from .models import ClientsList

# Adds all specified models to the admin panel

class ClientsListAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'email', 'password', 'reg_date')


admin.site.register(ClientsList, ClientsListAdmin)