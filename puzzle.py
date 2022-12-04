from game import Game

def getGames(data) -> Game :
    return Game(data)
    
with open('games.txt') as f:
    games = list(map(getGames, f.read().splitlines()))
print(games)
