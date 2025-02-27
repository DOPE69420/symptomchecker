from django.urls import path
from .views import get_diseases
from . import views

urlpatterns = [
    path('get_diseases/', get_diseases, name='get_diseases'),
    path('', views.index, name='index')
]
