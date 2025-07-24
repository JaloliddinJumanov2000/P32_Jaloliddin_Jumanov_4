
from Suggestion import views, admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),

]
