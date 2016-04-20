from card import Card
import random


class Deck(object):
	def __init__(self):
		self.cards = [] # a list of Card-object
		for number in Card.value_dict:
			for suit in 'sdhc':
				self.cards.append(Card(number, suit))
		random.shuffle(self.cards)
	
	def randomDraw(self):
		top = self.cards.pop()
		return top