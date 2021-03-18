from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('list/', views.taskListView.as_view(), name='list' ),
    path('create/', views.taskCreateView.as_view(), name='add'),
    path('update/<str:pk>/', views.taskUpdateiew.as_view(),name='task-update' ),
    path('detail/<str:pk>/', views.taskdetailView.as_view(),name='task-detail' ),
    path('delete/<str:pk>/', views.taskdeleteView.as_view(),name='task-delete' ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),),

]