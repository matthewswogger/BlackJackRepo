from player import Player
from deck import Deck
from dealer import Dealer
import random

class Game(object):
	def __init__(self):
		self.player = Player()
		self.deck = Deck()
		self.dealer = Dealer()
		self.isFirstDeal = True


	def dealToPlayer(self):
		if self.isFirstDeal:
			card1 = self.deck.randomDraw()
			card2 = self.deck.randomDraw()
			self.player.hand.extend([card1, card2])
			self.isFirstDeal = False
		else:
			card = self.deck.randomDraw()
			self.player.hand.append(card)
		pass
		
		print "Your Hand: ", self.player.hand
	
	def play_round(self):
		while self.player.play_action().low() == "h": #returns Hit or Stand"
			if self.player.choice.low() == "h":
				self.player.dealToPlayer()
			else: # end of the game
				self.player.hand
				self.dealer.play_action()
		
			
	def play_game(self):
		
			
			
			
			
if __name__ = '__main__':
	g = Game()
	g.play_game()