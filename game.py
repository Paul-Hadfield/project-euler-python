from hand import Hand

class Game:

    def __init__(self, data: str):
        self.player1 = Hand(data[0:14])   
        self.player2 = Hand(data[15:29])

    def __repr__(self):
        return 'P1: ' + self.player1.__repr__() + ', P2:' + self.player2.__repr__()
    def __str__(self):
        return 'P1: ' + self.player1.__str__() + ', P2:' + self.player2.__repr__()