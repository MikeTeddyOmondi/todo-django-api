from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tasks/list/', views.taskList, name="task-list"),
	path('tasks/detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('tasks/add/', views.taskCreate, name="task-create"),
	path('tasks/update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('tasks/delete/<str:pk>/', views.taskDelete, name="task-delete"),
]