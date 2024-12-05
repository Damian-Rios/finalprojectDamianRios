from django.urls import path
from . import views

app_name = 'sets'

urlpatterns = [
    path('', views.set_list, name='set_list'),  # Displays all sets by default
    path('search/', views.search_sets, name='search_sets'),  # Search sets based on filters
    path('view/<str:set_id>/', views.set_view, name='set_view'),
]
