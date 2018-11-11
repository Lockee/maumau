import player
import deck


class Maumau:
    def __init__(self, amount_of_players=2):
        self.deck_of_cards = deck.Deck(False)
        self.pile_of_cards = deck.Deck(True)
        self.players = []

        for i in range(amount_of_players):
            self.add_player()

        self.deal_cards_to_players()

    def deal_cards_to_players(self):
        amount_of_cards = 7 - len(self.players)
        for player in self.players:
            i = 0
            while i < amount_of_cards:
                player.add_card_to_hand(self.deck_of_cards.draw())
                i += 1

    def add_player(self):
        player_name = input("Please state your name player"+str(len(self.players)+1)+": ")
        self.players.append(player.Player(player_name))
