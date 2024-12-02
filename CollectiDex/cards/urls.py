from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('search/', views.search_cards, name='search_cards'),
    path('add/<str:card_id>/', views.add_card_to_collection, name='add_card_to_collection'),

]
