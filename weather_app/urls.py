# urls.py (inside the app)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
]
