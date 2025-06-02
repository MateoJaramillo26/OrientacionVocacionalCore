from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('calificaciones/', views.calificaciones, name='calificaciones'),
    path('asignarNota/', views.asignarNota, name='asignarNota'),
    path('logout/', views.exit, name='exit'),
]
