from django.urls import path
from . import views

urlpatterns = [
    path('recomendarCarrera/', views.RecomendarCarrera, name='recomendarCarrera')
]