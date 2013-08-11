from cards import *

class Player:

	def __init__(self):
		#player keeps track of his hand, health points, and name
		self.hand = []
		self.health_points = 7
		self.alias = ""

	def pull_card(self):
		while (len(self.hand) < 5):
			self.hand.append(deck.pop(0))