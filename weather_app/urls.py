# urls.py (inside the app)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weathers/', views.weather, name='weather'),
    path('forecast/', views.weather_forecast, name='forecast'),

]
