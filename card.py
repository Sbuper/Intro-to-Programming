__author__ = 'Andrew'
class Card():
    RANKS = {1,2,3,4,5,6,7,8,9,10,11,12,13}
    SUITS = {'Spades', 'Diamonds', 'Hearts', 'Clubs'}

    def __init__(self,suit,rank):
        self._suit = suit
        self._rank - rank

    def getRank(self):
        return(self._rank)

    def getSuit(self):
        return(self._suit)

    def __str__(self):
        if self._rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = str(self.rank)
        return rank + " of " +self.suit