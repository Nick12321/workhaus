class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def printCard(self):
        print(self.rank + " of " + self.suit)

class Deck:

    suits = ['Club', 'Diamonds', 'Heart', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(suit, rank)
                self.deck.append(card)

    def printDeck(self):
        for card in self.deck:
            card.printCard()

deck = Deck()
deck.printDeck()

def shuffleCard:
    for card in self.deck:


if __name__ == "__main__":
    myMainFunctionToRunApplication()
