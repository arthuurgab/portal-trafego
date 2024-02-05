from . import views
from django.urls import path

urlpatterns = [
    path('', views.cad_usuarios, name="cad_usuarios"),
]