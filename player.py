from cards import *

class Player:

	def __init__(self):
		self.hand = []
		self.cards_on_board = {}
		self.alias = ""


	def initialize_cards_on_board_data(self):
		self.cards_on_board["monster1"] = {}
		self.cards_on_board["monster2"] = {}
		self.cards_on_board["monster3"] = {}
		self.cards_on_board["monster1"]["heart"] = None
		self.cards_on_board["monster1"]["club"] = None
		self.cards_on_board["monster2"]["heart"] = None
		self.cards_on_board["monster2"]["club"] = None
		self.cards_on_board["monster3"]["heart"] = None
		self.cards_on_board["monster3"]["club"] = None
		self.cards_on_board["spade1"] = None
		self.cards_on_board["spade2"] = None
		self.cards_on_board["stun1"] = None
		self.cards_on_board["stun2"] = None

	def pull_card(self):
		#check for an empty deck
		if len(hand) == 0:
			hand.append(deck.pop(0))
			hand.append(deck.pop(0))
		else:
			hand.append(deck.pop(0))