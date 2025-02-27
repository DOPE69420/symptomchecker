from django.urls import path
from .views import get_diseases
from . import views
from .views import hello_world

urlpatterns = [
    path('get_diseases/', get_diseases, name='get_diseases'),
    path('', views.index, name='index'),
    path('api/hello/', hello_world, name='hello_world'),
]
