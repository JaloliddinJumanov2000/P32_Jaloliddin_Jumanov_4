from django.contrib import admin
from django.urls import path, include
from suggestions import views as suggestion_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', suggestion_views.suggestion_list, name='suggestion_list'),
    path('create/', suggestion_views.suggestion_create, name='suggestion_create'),
    path('edit/<int:pk>/', suggestion_views.suggestion_edit, name='suggestion_edit'),
    path('delete/<int:pk>/', suggestion_views.suggestion_delete, name='suggestion_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]
