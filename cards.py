from math import *
from dealer import *

class Card:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

class Heart(Card):
    def __init__(self, health, attack):
        Card.__init__(self,health,attack)
        self.name = str(health) + " of Hearts"
        self.attack = 0

    def buff(self, face_card):
        if (face_card.has_heart_buff()):
            print ("Cannot add another heart to this monster.")
        else:
            face_card.health = face_card.health + self.health
            face_card.heart_buff = self.health

    def debuff(self, opponent_face_card):
        if (opponent_face_card.has_heart_buff()):
            if (opponent_face_card.heart_buff > self.health):
                print ("Invalid Move. Opponents buff is stronger than your card's attempted debuff.")
            else:
                opponent_face_card.remove_heart_buff()
        else:
            print ("Invalid Move. The enemy monster does not have a heart to be debuffed.")

class Club(Card):
    def __init__(self, health, attack):
        Card.__init__(self,health,attack)
        self.name = str(attack) + " of Clubs"
        self.health = 0

    def buff(self, face_card):
        if (face_card.has_club_buff()):
            print ("Cannot add another club to this monster.")
        else:
            face_card.attack = face_card.attack + self.attack
            face_card.club_buff = self.attack

    def debuff(self, opponent_face_card):
        if (opponent_face_card.has_club_buff()):
            if (opponent_face_card.club_buff > self.attack):
                print ("Invalid Move. Opponents buff is stronger than your card's attempted debuff.")
            else:
                opponent_face_card.remove_club_buff()
        else:
            print ("Invalid Move. The enemy monster does not have a club to be debuffed.")

class Face_Card(Card):
    def __init__(self, health, attack):
        Card.__init__(self,health,attack)
        self.stunned = False
        self.heart_buff = 0
        self.club_buff = 0


    def has_heart_buff(self):
        if (self.heart_buff == 0):
            return False
        return True

    def remove_heart_buff(self):
        if ((self.health - self.heart_buff) < 1):
            self.health = 1
        else:
            self.health = self.health - self.heart_buff
            self.heart_buff = 0
            print ("removing heart buff")

    def has_club_buff(self):
        if (self.club_buff == 0):
            return False
        return True

    def remove_club_buff(self):
        self.club_buff = 0

        
    def is_stunned(self):
        return self.stunned

    def attack(self, opponent_face_card):
        if not stunned:
            opponent_face_card.health = opponent_face_card.health - self.attack

    def is_dead(self):
        if not (self.health > 0):
            Board.move_to_graveyard(self)
            return True
        return False

class Diamond(Card):
    def __init__(self,value):
        self.value = value
        self.name = str(value) + " of Diamonds"

    def stun(self, opponent_face_card):
        if Board.has_opponent_stun_card:
            if (opponent.stun_card_value > self.value):
                print ("Cannot play stun card, as enemy stun card is higher.")
            else:
                opponent_face_card.stunned = true
        else:
            opponent_face_card.stunned = true


class Spade(Card):
    def __init__(self, value):
        self.value = value
        self.name = str(value) + " of Spades"

   # def construct(self):
