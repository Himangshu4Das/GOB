from django.contrib import admin
from django.urls import path, include
from base.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('base.urls')),
    path('', home_view, name='home'),
    path('', include('accounts.urls')),
    path('delegator/', include('delegator.urls')),
    path('evaluator/', include('evaluator.urls')),
    path('iotclump/', include('iotclump.urls')),
]
