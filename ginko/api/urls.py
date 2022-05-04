from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('action/', get_action),
    path('action/<int:pk>/', get_action_detail)
]