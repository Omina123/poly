from Home.views import *
from django.urls import path,include
from django.contrib import admin
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', home, name='home'),
        path('notice_notice/', create_notice, name='create_notice'),
        path('council/', council, name='council'),
        path('higher_diploma/', Higher_diploma, name='higher_diploma'),
        path('diploma/', diploma, name='diploma'),
        path('certif/', certificate, name='certificate'),
        path('artisan/', artisan, name='artisan'),



]
