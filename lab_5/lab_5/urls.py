from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainPage', include('Tourism.urls')),
    path('tstpage', HttpResponse("google.com"))
]
