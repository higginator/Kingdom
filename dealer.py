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

	def make_spades(self):

	def make_face_cards(self):



	#initial deal of cards, 5 per player
	def deal_cards(self, playerOne, playerTwo):
		if (Game.current_round == 1):
			for x in range(5):
				PlayerOne.hand.append(deck.pop(0))
				PlayerTwo.hand.append(deck.pop(0))