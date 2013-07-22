from cards import *

class Dealer:
	def __init__(self):
		self.deck = []

	def make_hearts(self):
		for i in range(2,11):
			self.deck.append(Heart(i,0))

	def make_diamonds(self):
		for i in range(2,11):
			self.deck.append(Diamond(i))

	def make_clubs(self):
		for i in range(2,11):
			self.deck.append(Club(0,i))