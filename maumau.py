import player
import deck
import sys
import os


class Maumau:
    def __init__(self, amount_of_players=2):
        self.deck_of_cards = deck.Deck(False)
        self.pile_of_cards = deck.Deck(True)
        self.amount_of_players = amount_of_players
        self.players = []

        for i in range(self.amount_of_players):
            self.add_player()

        self.deal_cards_to_players()
        self.pile_of_cards.add_card_to_stack(self.deck_of_cards.draw())

    def deal_cards_to_players(self):
        amount_of_cards = 7 - len(self.players)
        for player in self.players:
            i = 0
            while i < amount_of_cards:
                player.add_card_to_hand(self.deck_of_cards.draw())
                i += 1

    def add_pile_to_deck(self):
        new_pile = [self.pile_of_cards.draw()]
        self.deck_of_cards.add_stack_to_deck(self.pile_of_cards)
        self.pile_of_cards = new_pile

    def add_player(self):
        player_name = input("Please state your name player"+str(len(self.players)+1)+": ")
        self.players.append(player.Player(player_name))

    def start_game(self):
        players_turn = 0
        while True:
            self.clear_screen()
            top_card = self.pile_of_cards.top()
            curr_player = self.players[players_turn]
            print("===Top of Pile===")
            print(top_card)
            print("=================")
            print("it's", curr_player.name + "s", "turn.\n")
            print(curr_player)
            curr_player_card_index = -1
            while True:
                try:
                    curr_player_card_index = int(input("Which card do you want to play?: ")) - 1
                    if curr_player_card_index >= len(curr_player) or curr_player_card_index < 0:
                        print("Number does not fit your hand! Please state a valid card.")
                    else:
                        break
                except ValueError:
                    print("please only enter a valid number.")
            self.pile_of_cards.add_card_to_stack(curr_player.play_card(curr_player_card_index))
            print("played card:", self.pile_of_cards.top())
            print(curr_player)
            players_turn = (players_turn + 1) % self.amount_of_players
            input("next turn")

    @staticmethod
    def clear_screen():
        os.system('clear') if sys.platform != "windows" else os.system('cls')
