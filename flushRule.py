from card import CardValue
from game import Game
from hand import Hand

def isFlush(hand: Hand) -> bool:
    return len(hand.suites) != 1

def flushRule(game: Game) -> int:
    p1IsFlush = isFlush(game.player1)
    p2IsFlush = isFlush(game.player2)
    if p1IsFlush and not p2IsFlush:
        return 1
    if p2IsFlush and not p1IsFlush:
        return 2
    return 0   