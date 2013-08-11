from cards import *
from random import shuffle
class Dealer:
	def __init__(self):
		#dealer class holds the deck, makes the cards, and shuffles the cards
		self.deck = []
		self.make_hearts()
		self.make_diamonds()
		self.make_clubs()
		#self.make_spades()
		#self.make_face_cards()

	def make_hearts(self):
		for i in range(2,11):
			self.deck.append(Heart(i,0))

	def make_diamonds(self):
		for i in range(2,11):
			self.deck.append(Diamond(i))

	def make_clubs(self):
		for i in range(2,11):
			self.deck.append(Club(0,i))

	#def make_spades(self):

	#def make_face_cards(self):



	#initial deal of cards, 5 per player
	def deal_cards(self, player_one, player_two):
		if (Game.current_round == 1):
			for x in range(5):
				player_one.hand.append(deck.pop(0))
				player_two.hand.append(deck.pop(0))

	def shuffle_deck(self):
		shuffle(deck)