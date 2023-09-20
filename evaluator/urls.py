from django.urls import path
from . import views

# app_name = 'evaluator'
urlpatterns = [
    path('evaluator/', views.evaluator_view, name='evaluator'),
    # Other URL patterns for the 'evaluator' app
]
