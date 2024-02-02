from django.contrib import admin
from django.urls import path, include
from app_homepage import urls as homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(homepage)),
]
