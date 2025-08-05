# podcasts/urls.py
from django.urls import path
from .views import upload_audio

urlpatterns = [
    path('admin/upload-audio/', upload_audio, name='upload_audio'),
]