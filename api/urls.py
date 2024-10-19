from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.tasks),
    path('tasks/<int:pk>', views.task_by_id),
    path('cadastro', views.cadastro),
]