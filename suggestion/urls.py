from django.urls import path
from . import views

urlpatterns = [
    path('', views.suggestion_list, name='suggestion_list'),
    path('create/', views.suggestion_create, name='suggestion_create'),
    path('<int:pk>/', views.suggestion_detail, name='suggestion_detail'),
    path('<int:pk>/update/', views.suggestion_update, name='suggestion_update'),
    path('<int:pk>/delete/', views.suggestion_delete, name='suggestion_delete'),
    path('register/', views.register, name='register'),
]