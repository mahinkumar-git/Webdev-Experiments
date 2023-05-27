"""Places_around_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from interactive_map import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="mainpage"),
    path('Anna_Stadium/', views.Anna_Stadium, name="Anna_Stadium"),
    path('Cuddalore_post_office/', views.postoffice),
    path('Gedilam_River_Bridge/', views.bridge),
    path('Cuddalore_Bus_Stand/',views.busstand),
    path('Cuddalore_railway_station/',views.railway)
]