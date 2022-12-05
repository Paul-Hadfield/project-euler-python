from game import Game
from royalFlushRule import royalFlushRule
from flushRule import flushRule
from highestCardRule import highestCardRule

def getGames(data) -> Game :
    return Game(data)
    
def playGame(game: Game) -> int:

    #Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    winner = royalFlushRule(game)
    if winner != 0:
        return winner

    #Straight Flush: All cards are consecutive values of same suit.
    #Four of a Kind: Four cards of the same value.
    #Full House: Three of a kind and a pair.

    #Flush: All cards of the same suit.
    winner = flushRule(game)
    if winner != 0:
        return winner

    #Straight: All cards are consecutive values.
    #Three of a Kind: Three cards of the same value.
    #Two Pairs: Two different pairs.
    #One Pair: Two cards of the same value.

    #High Card: Highest value card.
    winner = highestCardRule(game)
    if winner == 0:
        raise NameError('Should be no draw')
    return winner

def player1Wins(winner:int) -> bool:
    return winner != 1

with open('games.txt') as f:
    games = list(map(getGames, f.read().splitlines()))
    count = len(list(filter(player1Wins, map(playGame, games))))
    print(count)