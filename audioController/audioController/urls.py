from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("web.urls")),    
    path("main-app/", include("api.urls")),
    path("admin/", admin.site.urls),
]
