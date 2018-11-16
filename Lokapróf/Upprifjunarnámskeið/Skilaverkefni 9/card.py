class Card(object):

    def __init__(self, _rank, _suit):

        self.rank = _rank
        self.suit = _suit

    def __str__(self):
        if self.is_blank():
            print("BLK")
        else:
            print('{0:>3d}{1}'.format(self.rank, self.suit))
    def is_blank(selfs):
        return self.rank == 0 and self.suit == ""