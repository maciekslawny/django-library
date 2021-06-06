from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('biblioteka/', include('Biblioteka.urls')),
    path('admin/', admin.site.urls),
]
