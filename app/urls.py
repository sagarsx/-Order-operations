from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('order/', views.add_order, name="order"),
    path('delete/<str:pk>/', views.delete_order, name="delete"),
    path('edit/<str:pk>/', views.edit_order, name="edit")
]