from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_list, name='set_list'),  # Displays all sets by default
    path('search/', views.search_sets, name='search_sets'),  # Search sets based on filters
]
