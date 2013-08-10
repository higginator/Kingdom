from dealer import *
from board import *
from cards import *
from player import *

class Game:
	def __init__(self):
		#self.id = (Get Total Database Games) + 1
		self.player_one = Player()
		self.player_two = Player()
		self.current_round = 0
		self.board = Board()
		self.dealer = Dealer()