from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.intro_socio, name='intro_socio'),
    path('show/', views.show_socios, name='show_socios'),
    path('change/', views.chang_pass, name='change_pass'),
    path('count_pass/', views.count_pass_iguales, name='count_pass_iguales'),
]