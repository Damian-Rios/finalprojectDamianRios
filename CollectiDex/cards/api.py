from dataclasses import dataclass
from typing import Optional, List
from pokemontcgsdk import RestClient
from django.conf import settings
from pokemontcgsdk.card import Card as PokeCard  # Renaming imported Card to avoid conflict

from pokemontcgsdk.ability import Ability
from pokemontcgsdk.ancienttrait import AncientTrait
from pokemontcgsdk.attack import Attack
from pokemontcgsdk.cardimage import CardImage
from pokemontcgsdk.legality import Legality
from pokemontcgsdk.querybuilder import QueryBuilder
from pokemontcgsdk.resistance import Resistance
from pokemontcgsdk.set import Set
from pokemontcgsdk.tcgplayer import TCGPlayer
from pokemontcgsdk.cardmarket import Cardmarket
from pokemontcgsdk.weakness import Weakness

RestClient.configure('f89e3fab-3136-4936-971b-c171d0f4782d')

@dataclass
class CustomCard:
    RESOURCE = 'cards'

    abilities: Optional[List[Ability]]
    artist: Optional[str]
    ancientTrait: Optional[AncientTrait]
    attacks: Optional[List[Attack]]
    cardmarket: Optional[Cardmarket]
    convertedRetreatCost: Optional[int]
    evolvesFrom: Optional[str]
    flavorText: Optional[str]
    hp: Optional[str]
    id: str
    images: CardImage
    legalities: Legality
    regulationMark: Optional[str]
    name: str
    nationalPokedexNumbers: Optional[List[int]]
    number: str
    rarity: Optional[str]
    regulationMark: Optional[str]
    resistances: Optional[List[Resistance]]
    retreatCost: Optional[List[str]]
    rules: Optional[List[str]]
    set: Set
    subtypes: Optional[List[str]]
    supertype: str
    tcgplayer: Optional[TCGPlayer]
    types: Optional[List[str]]
    weaknesses: Optional[List[Weakness]]

    @staticmethod
    def find(id):
        return QueryBuilder(CustomCard, CustomCard.transform).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(CustomCard, CustomCard.transform).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(CustomCard, CustomCard.transform).all()

    @staticmethod
    def transform(response):
        if response.get('tcgplayer', {}).get('prices', {}).get('1stEditionNormal'):
            response['tcgplayer']['prices']['firstEditionNormal'] = response['tcgplayer']['prices'].pop('1stEditionNormal')
        if response.get('tcgplayer', {}).get('prices', {}).get('1stEditionHolofoil'):
            response['tcgplayer']['prices']['firstEditionHolofoil'] = response['tcgplayer']['prices'].pop('1stEditionHolofoil')
        return response


def test_cards():
    # Fetching all cards
    cards = CustomCard.all()  # Fetching all cards
    print(f"Found {len(cards)} cards.")
    for card in cards:
        print(f"Card: {card.name}, HP: {card.hp}")


if __name__ == "__main__":
    test_cards()
