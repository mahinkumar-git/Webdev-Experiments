
from django.contrib import admin
from django.urls import path
from timetableapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="mainpage")
]
