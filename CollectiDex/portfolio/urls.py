from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('collection/', views.collection, name='collection'),
]