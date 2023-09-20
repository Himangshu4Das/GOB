from django.urls import path
from . import views

# app_name= 'delegator'
urlpatterns = [
    path('delegator/', views.delegator_view, name='delegator'),
    # Other URL patterns for the 'delegator' app
]
