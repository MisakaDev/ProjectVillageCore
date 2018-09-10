"""ProjectVillageCore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Auth
    path('api/v1/auth/', include('auth.urls')),
    # Profiles
    path('api/v1/profiles/', include('profiles.urls')),
    # Address
    path('api/v1/address/', include('address.urls')),
    # Persons
    path('api/v1/persons/', include('persons.urls')),
]
