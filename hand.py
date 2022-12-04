from card import CardValue
from card import Card

def sortValue(card: Card) -> int:
    return card.value.value

class Hand:

    def __init__(self, data: str):
        self.cards:list[Card] = []     
        self.cards.append(Card(data[0:2]))
        self.cards.append(Card(data[3:5]))
        self.cards.append(Card(data[6:8]))
        self.cards.append(Card(data[9:11]))
        self.cards.append(Card(data[12:14]))
        self.cards.sort(reverse=True, key=sortValue)

    def __repr__(self):
        return self.cards.__repr__()
    def __str__(self):
        return self.cards.__str__()