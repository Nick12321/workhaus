import random

NUMBER_OF_CARD_IN_DECK = 52

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def printCard(self):
		print(self.rank + " of " + self.suit)

class Deck:

	suits = ['Club', 'Dimonds', 'Heart', 'Spades']
	ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']

	def __init__(self):
		self.deck = []
		for suit in self.suits:
			for rank in self.ranks:
				card = Card(suit, rank)
				self.deck.append(card)

	def shuffle(self):
		index = 0
		while index < NUMBER_OF_CARD_IN_DECK:
			randomPick = random.randint(0, NUMBER_OF_CARD_IN_DECK - 1)
			#print(randomPick)
			card1 = self.deck[index]
			card2 = self.deck[randomPick]
			self.deck[index] = card2
			self.deck[randomPick] = card1
			index += 1



	def printDeck(self):
		for card in self.deck:
			card.printCard()
		print("Total card: " + str(len(self.deck)))

deck = Deck()
deck.shuffle()
deck.printDeck()
