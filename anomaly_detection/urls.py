# urls.py
from django.urls import path
from api.views import create_detection_data

urlpatterns = [
    path('api/data/', create_detection_data),
]
