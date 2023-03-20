from django.conf.urls import url, include
from .views import ClientsListView

# Specify the path to the database

urlpatterns = [
    url(r'^$', ClientsListView.as_view()),
]