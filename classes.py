from data.cards import cards
from data.spreads import spreads
import random

class Card:
    def __init__(self, card: dict):
        self.name = card['name']
        self.reversed = random.random() > 0.5
        self.description = card['desc'] if not self.reversed else card['rdesc']

class Deck:
    def __init__(self):
        self.cards = cards
        random.shuffle(self.cards)
    
class Spread:
    def __init__(self, spread_name: str):
        self.spread_name = spreads[spread_name]
        self.spread = self.draw_spread()
    
    def draw_spread(self):
        deck = Deck()
        d = []
        for position in self.spread_name:
            card = Card(deck.cards.pop())
 
            d.append({
                    "position": position,
                    "name": card.name,
                    "reversed": card.reversed,
                    "description": card.description
                })
        
        return d
