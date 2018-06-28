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
        import random
        length = len(self.deck)
        self.random = []
        self.random = self.deck
        while length != 0:
            position = random.randint(0, (length - 1))
            randomCard = self.random[position]
            randomCard.printCard()
            del self.random[position]
            length -= 1
        print('==========')
        randomCount = len(self.random)
        deckCount = len(self.deck)
        print("Number of cards left in Random:")
        print(randomCount)

    def printDeck(self):
        for card in self.deck:
            card.printCard()

deck = Deck()
deck.printDeck()
