from django.urls import path

from index import views

app_name = 'todo'
urlpatterns = [

    path('', views.task_list, name='list'),
    path('addlist/', views.addlist, name="addlist"),
    path('completed/<str:pk>/', views.taskComplete, name='completed'),
    path('task_delete/<str:pk>/', views.taskDelete, name='delete')
]
