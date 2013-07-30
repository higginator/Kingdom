class Board:
	def __init__(self):
		#monster (heart,club), monster (heart,club), monster (heart,club), spade, spade, stun, stun
		self.playerOne = {}
		self.playerTwo = {}

	def initialize_board(self):
		self.playerOne["monster1"] = {}
		self.playerOne["monster2"] = {}
		self.playerOne["monster3"] = {}
		self.playerOne["monster1"]["heart"] = None
		self.playerOne["monster1"]["club"] = None
		self.playerOne["monster2"]["heart"] = None
		self.playerOne["monster2"]["club"] = None
		self.playerOne["monster3"]["heart"] = None
		self.playerOne["monster3"]["club"] = None
		self.playerOne["spade1"] = None
		self.playerOne["spade2"] = None
		self.playerOne["stun1"] = None
		self.playerOne["stun2"] = None

		self.playerTwo["monster1"] = {}
		self.playerTwo["monster2"] = {}
		self.playerTwo["monster3"] = {}
		self.playerTwo["monster1"]["heart"] = None
		self.playerTwo["monster1"]["club"] = None
		self.playerTwo["monster2"]["heart"] = None
		self.playerTwo["monster2"]["club"] = None
		self.playerTwo["monster3"]["heart"] = None
		self.playerTwo["monster3"]["club"] = None
		self.playerTwo["spade1"] = None
		self.playerTwo["spade2"] = None
		self.playerTwo["stun1"] = None
		self.playerTwo["stun2"] = None