
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DrAi/', include('DrAi.urls')),
    path('', include('DrAi.urls')),
]

