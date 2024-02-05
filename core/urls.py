from django.contrib import admin
from django.urls import path, include
from app_homepage import urls as homepage
from app_control_panel import urls as control_panel
from app_cad_usuarios import urls as cad_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(homepage)),
    path('control_panel/', include(control_panel)),
    path('cad_usuarios/', include(cad_usuarios)),
]
