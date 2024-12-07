from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('collection_cards/', views.cards_in_collection, name='collection_cards'),
    path('collection_sets/', views.sets_in_collection, name='collection_sets'),
    path('type/<str:card_type>/', views.cards_by_type, name='cards_by_type'),  # Cards per type
    path('rarity/<str:rarity>/', views.cards_by_rarity, name='cards_by_rarity'),  # Cards per rarity
]