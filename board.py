from Player import *
class Board:
	def __init__(self):
		#monster (heart,club), monster (heart,club), monster (heart,club), spade, spade, stun, stun
		self.playerOne = {}
		self.playerTwo = {}

	def initialize_board(self):
		PlayerOne.initialize_cards_on_board_data()
		PlayerTwo.initialize_cards_on_board_data()