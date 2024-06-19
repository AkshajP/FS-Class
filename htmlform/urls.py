from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('form/', home_view, name="home"),
]