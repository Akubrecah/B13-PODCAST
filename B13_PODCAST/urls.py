from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from podcasts.views import upload_audio  # Correct import position

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/upload-audio/', upload_audio, name='upload_audio'),
    path('admin/', admin.site.urls),
    path('podcasts/', include('podcasts.urls')),
]
    # Add other app URLs as needed
    # path('podcasts/', include('podcasts.urls')),
    # path('users/', include('users.urls')),

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)