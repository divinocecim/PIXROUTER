from django.contrib import admin
from django.urls import path, include
from api_rest import models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls')),
]
