from django.urls import path
from .views import get_diseases,voice_input
from . import views
from .views import hello_world

urlpatterns = [
    path('get_diseases/', get_diseases, name='get_diseases'),
    path('', views.index, name='index'),
    path('api/hello/', hello_world, name='hello_world'),
    path("voice-input/", voice_input, name="voice_input"),
]
