from django.contrib import admin
from django.urls import path, include

from api_rest.api import viewsets

urlpatterns = [
    path('', viewsets.get_all_pix),
    path('v1/data/<int:textid>', viewsets.get_by_textid),
    path('v1/enviapix/', viewsets.pix_manager),
    path('v1/deleta_hist/', viewsets.pix_delete),
    path('v1/chavespix/', viewsets.get_all_keys),
]
