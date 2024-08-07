from django.urls import path
from .views import main, mainApp

urlpatterns = [
    path("main-app/1", main),
    path("main-app", mainApp),
]
