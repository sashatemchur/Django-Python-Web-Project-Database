from django.conf.urls import url, include
from django.contrib import admin

# Specifies the path to the given forces 

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', include('database.urls')),
]