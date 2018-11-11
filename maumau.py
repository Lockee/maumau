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

    def compare_card_with_top_of_pile(self, card):
        return self.pile_of_cards.card_is_playable(card)

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
            print(curr_player, "d. Draw a Card", sep="")
            card_index = -1
            card_drawn = False
            while True:
                card_index = input("Which card do you want to play?: ")
                if card_index.isdigit():
                    card_index = int(card_index) - 1
                    if card_index >= len(curr_player) or card_index < 0:
                        print("Number does not fit your hand! Please state a valid card.")
                        continue
                elif card_index.lower() == "d":
                    drawn_card = self.deck_of_cards.draw()
                    print(drawn_card, "has been drawn")
                    curr_player.add_card_to_hand(drawn_card)
                    card_index = -1
                    card_drawn = True
                else:
                    print("Please enter valid input")
                    continue
                
                if(self.compare_card_with_top_of_pile(curr_player.hand[card_index])):
                    self.pile_of_cards.add_card_to_stack(
                        curr_player.play_card(card_index))
                    if curr_player.last_card():
                        print("MAUMAU!")
                    print("played card:", self.pile_of_cards.top())
                    break
                elif card_drawn:
                    print("No card has been played")
                    break
                else:
                    print("Card cannot be played! Choose another card.")
            if curr_player.hand_is_empty():
                print(curr_player.name, "has won")
                break
            players_turn = (players_turn + 1) % self.amount_of_players
            input("next turn")

    @staticmethod
    def clear_screen():
        os.system('clear') if sys.platform != "windows" else os.system('cls')
