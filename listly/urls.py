from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.addTask, name='add_task'),
    path('update_tasks/<str:pk>/', views.update_tasks, name='update_tasks'),
    path('delete_task/<str:pk>/', views.delete_task, name='delete_task'),
]



