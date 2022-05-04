from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('action', views.get_action)
]