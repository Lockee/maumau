"""Player class, it contains the name of the player, hand of cards
    and the final score"""


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def play_card(self, card_index):
        """returns last card object in hand and removes it"""
        return self.hand.pop(card_index)

    def add_card_to_hand(self, card):
        """adds a card object to the players hand"""
        self.hand.append(card)

    def last_card(self):
        """returns true if only one card is left"""
        return len(self.hand) == 1

    def hand_is_empty(self):
        """returns true if no cards are left"""
        return len(self.hand) == 0

    def __len__(self):
        """len of a player is the length of its hand"""
        return len(self.hand)

    def __str__(self):
        """pretty print of the player"""
        hand = ""
        for i, card in enumerate(self.hand):
            hand += str(i+1) + ". " + str(card) + "\n"
        return self.name + "s hand:\n" + hand
