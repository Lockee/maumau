class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def play_card(self, card_index):
        return self.hand.pop(card_index)

    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def last_card(self):
        return len(self.hand) == 1

    def hand_is_empty(self):
        return len(self.hand) == 0

    def __len__(self):
        return len(self.hand)

    def __str__(self):
        hand = ""
        for i, card in enumerate(self.hand):
            hand += str(i+1) + ". " + str(card) + "\n"
        return self.name + "s hand:\n" + hand