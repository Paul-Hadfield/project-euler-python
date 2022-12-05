from game import Game

def highestCardRule(game: Game) -> int:
    index = 0
    while(index < 5):
        if game.player1.cards[index].value.value > game.player2.cards[index].value.value:
            return 1
        if game.player2.cards[index].value.value > game.player1.cards[index].value.value:
            return 2
        index += 1
    return 0