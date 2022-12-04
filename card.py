from enum import Enum

class CardValue(Enum):
    TWO = 2
    THREE = 3 
    FOUR = 4 
    FIVE = 5 
    SIX = 6
    SEVEN = 7 
    EIGHT = 8 
    NINE = 9 
    TEN = 10 
    JACK = 11 
    QUEEN = 12 
    KING = 13
    ACE = 14

class CardSuite(Enum):
    HEARTS = 'H'
    CLUBS = 'C'
    DIAMONDS = 'D'
    SPADES = 'S'

def parseCardValue(value:str)-> CardValue:
    match value:
        case '2':
            return CardValue.TWO
        case '3':
            return CardValue.THREE
        case '4':
            return CardValue.FOUR
        case '5':
            return CardValue.FIVE
        case '6':
            return CardValue.SIX
        case '7':
            return CardValue.SEVEN
        case '8':
            return CardValue.EIGHT
        case '9':
            return CardValue.NINE
        case 'T':
            return CardValue.TEN
        case 'J':
            return CardValue.JACK
        case 'Q':
            return CardValue.QUEEN
        case 'K':
            return CardValue.KING
        case 'A':
            return CardValue.ACE
        case _:
            raise NameError('Unknown value')

def parseCardSuite(value: str) -> CardSuite:
    match value:
        case 'H':
            return CardSuite.HEARTS
        case 'D':
            return CardSuite.DIAMONDS
        case 'S':
            return CardSuite.SPADES
        case 'C':
            return CardSuite.CLUBS
        case _:
            raise NameError('Unknown value')

class Card:
    def __init__(self, data: str):
        self.value = parseCardValue(data[0])
        self.suite = parseCardSuite(data[1])

    def __repr__(self):
        return self.value.name + ':' + self.suite.value
    def __str__(self):
        return self.value.name + ':' + self.suite.value