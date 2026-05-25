import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 1. This must be EXACTLY admin.site.urls
    path('admin/', admin.site.urls),  
    
    # 2. Connects your Home app routing setup
    path('', include('Home.urls')),   
]

# 3. Serve uploaded files locally during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)