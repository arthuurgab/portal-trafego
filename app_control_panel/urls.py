from . import views
from django.urls import path

urlpatterns = [
    path('', views.panel, name="control_panel"),
    path('usuarios/', views.usuarios, name="usuarios")
]