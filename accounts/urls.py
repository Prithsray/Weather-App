# accounts/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.default_view, name='default'),
    path('weather/', include('weather_app.urls')),    # Main Weather App URLs

]
