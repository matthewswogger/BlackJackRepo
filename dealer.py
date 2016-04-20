class Dealer(object):
	def __init__(self):
		self.cards = []
		self.total = 0
		
	
	def play_action(self):
		#first draw 
		
		
	def count_score(self):
		self.total = 0
		for card in self.cards: # each item in self.cards is a Card-object
			self.total = self.total + value_dict[card.number]

					
