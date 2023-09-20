from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.home_view, name='home'),
    # path('delegator/', views.page1_view, name='delegator'),
    # path('evaluator/', views.page2_view, name='evaluator'),
]