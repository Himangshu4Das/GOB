from django.urls import path
from . import views

urlpatterns = [
    path('iotclump/', views.iotclump_view, name='iotclump'),
]
