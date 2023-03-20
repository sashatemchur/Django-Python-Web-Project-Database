from django.shortcuts import render
from django.views.generic import ListView
from .models import ClientsList

# We make a client model

class ClientsListView(ListView):
    model = ClientsList