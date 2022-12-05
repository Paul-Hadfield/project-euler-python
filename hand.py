from functools import reduce
from card import CardValue
from card import CardSuite
from card import Card

def sortValue(card: Card) -> int:
    return card.value.value

def getSuites(suites: dict[CardSuite, int], card:Card) -> dict[CardSuite, int]:
    suites[card.suite.name] = (suites.get(card.suite.name) or 0) + 1
    return suites

def getValues(values: dict[CardValue, int], card:Card) -> dict[CardValue, int]:
    values[card.value.name] = (values.get(card.value.name) or 0) + 1
    return values

class Hand:

    def __init__(self, data: str):
        self.cards:list[Card] = []     
        self.cards.append(Card(data[0:2]))
        self.cards.append(Card(data[3:5]))
        self.cards.append(Card(data[6:8]))
        self.cards.append(Card(data[9:11]))
        self.cards.append(Card(data[12:14]))
        self.cards.sort(reverse=True, key=sortValue)
        self.suites = reduce(getSuites, self.cards, {})
        self.values = reduce(getValues, self.cards, {})
        
    def __repr__(self):
        return self.cards.__repr__()
    def __str__(self):
        return self.cards.__str__()