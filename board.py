class Board:
	def __init__(self):
		#monster (heart,club), monster (heart,club), monster (heart,club), spade, spade, stun, stun
		self.player_one_side = {}
		self.player_two_side = {}
		self.initialize_board()

	def initialize_board(self):
		self.initialize_player_board_data(self.player_one_side)
		self.initialize_player_board_data(self.player_two_side)

	def initialize_player_board_data(self, player_dictionary):
		player_dictionary["monster1"] = {}
		player_dictionary["monster2"] = {}
		player_dictionary["monster3"] = {}
		player_dictionary["monster1"]["heart"] = None
		player_dictionary["monster1"]["club"] = None
		player_dictionary["monster2"]["heart"] = None
		player_dictionary["monster2"]["club"] = None
		player_dictionary["monster3"]["heart"] = None
		player_dictionary["monster3"]["club"] = None
		player_dictionary["spade1"] = None
		player_dictionary["spade2"] = None
		player_dictionary["stun1"] = None
		player_dictionary["stun2"] = None

