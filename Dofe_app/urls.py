from django.urls import path
from . import views

urlpatterns = [
    path('classroom_reservation/', views.classroom_reservation, name='classroom_reservation'),
    path('classroom_reservation/add/', views.add_classroom_reservation, name='add_classroom_reservation'),
]