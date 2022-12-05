from card import CardValue
from game import Game
from hand import Hand

def isRoyalFlush(hand: Hand) -> bool:
    if len(hand.suites) != 1:
        return False
    if hand.cards[0].value != CardValue.ACE:
        return False
    if hand.cards[1].value != CardValue.KING:
        return False
    if hand.cards[2].value != CardValue.QUEEN:
        return False
    if hand.cards[3].value != CardValue.JACK:
        return False
    if hand.cards[4].value != CardValue.TEN:
        return False
    return True

def royalFlushRule(game: Game) -> int:
    p1IsRF = isRoyalFlush(game.player1)
    p2IsRF = isRoyalFlush(game.player2)
    if p1IsRF and not p2IsRF:
        return 1
    if p2IsRF and not p1IsRF:
        return 2
    return 0   