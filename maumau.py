import player
import stackOfCards
import sys
import os


class Maumau:
    def __init__(self):
        """initializes the game, creates 2 deck object and adds the given
            amount of players, each player is given cards from the deck"""
        self.deck_of_cards = stackOfCards.StackOfCards(False)
        self.pile_of_cards = stackOfCards.StackOfCards(True)
        self.amount_of_players = self.set_amount_of_players()
        self.players = []
        self.turn = 0
        self.curr_player = None
      
        self.name_players()
        self.deal_cards_to_players()
        self.pile_of_cards.add_card_to_stack(self.deck_of_cards.draw())

    def name_players(self):
        self.players = []
        for i in range(self.amount_of_players):
            player_name = input("Please state your name player"+str(i+1)+": ")
            new_player = player.Player(player_name)
            self.players.append(new_player)

    def set_amount_of_players(self):
        while True:
            amount_of_players = input("How many players are playing(2-4): ")
            if amount_of_players.isdigit() and 2 <= int(amount_of_players) <= 4:
                return int(amount_of_players)
            else:
                print("the number has to be between 2 and 4")

    def deal_cards_to_players(self):
        amount_of_cards = 7 - len(self.players)
        for player in self.players:
            i = 0
            while i < amount_of_cards:
                player.add_card_to_hand(self.deck_of_cards.draw())
                i += 1

    def add_pile_to_deck(self):
        """adds every but the last card object from the pile to the deck"""
        new_pile = stackOfCards.StackOfCards(True, [self.pile_of_cards.draw()])
        self.deck_of_cards.pile_onto_deck(self.pile_of_cards)
        self.pile_of_cards = new_pile

    def is_card_valid(self, card):
        """compares the card with the last card of the pile"""
        return self.pile_of_cards.card_is_playable(card)

    def rule_card_seven(self):
        pass

    def rule_card_eight(self):
        pass

    def rule_card_jack(self):
        pass

    def score_count(self):
        """adds a scoure to the players based on their cards left:
            Cards 7-10 Points corresponding to their print
            10 Points for a Queen or a King
            11 Points for an Ace
            20 Point for a Jack"""
        for player in self.players:
            for card in player.hand:
                if card.num.isdigit():
                    player.score += int(card.num)
                elif card.num == "Ace":
                    player.score += 11
                elif card.num == "Jack":
                    player.score += 20
                else:
                    player.score += 10
        self.players.sort(key=lambda player: player.score)
        print("Your Score: ")
        for i, player in enumerate(self.players):
            print(str(i+1)+".", player.name + ":", str(player.score))

    def next_turn(self):
        # TODO: add to logic
        self.turn = (self.turn + 1) % 4
        self.curr_player = self.players[self.turn]

    def reshuffle_deck(self):
        if self.deck_of_cards.is_empty():   # pile reshuffeld into deck
                self.add_pile_to_deck()
                self.deck_of_cards.shuffle()

    def player_action(self):
        # TODO: replace in logic
        while True:
            card_index = input("Which card do you want to play?: ")
            if card_index.isdigit():
                card_index = int(card_index) - 1
                if card_index >= len(self.curr_player) or card_index < 0:
                    print("Number does not fit your hand! Please state a valid card.")
                    continue
            elif card_index.lower() == "d":
                drawn_card = self.deck_of_cards.draw()
                print(drawn_card, "has been drawn")
                self.curr_player.add_card_to_hand(drawn_card)
                card_index = -1
                card_drawn = True
            else:
                print("Please enter valid input")
                continue

    def start_game(self):
        """Starts a game of MauMau - it's the games Skeleton"""
        players_turn = 0
        while True:  # Game Loop
            self.clear_screen()
            self.reshuffle_deck()
            # ==== info prints ====
            print("Amount of cards in deck left:", len(self.deck_of_cards))
            print("Amount of cards on pile:", len(self.pile_of_cards))
            top_card = self.pile_of_cards.top()
            curr_player = self.players[players_turn]
            for player in self.players:
                if player is curr_player:
                    continue
                print("Amount of cards in", player.name + "s hand:", len(player))

            print("===Top of Pile===")
            print(top_card)
            print("=================")
            print("it's", curr_player.name + "s", "turn.\n")
            print(curr_player, "d. Draw a Card", sep="")
            card_index = -1
            card_drawn = False

            while True:  # player input loop
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
                # put card into pile
                if(self.is_card_valid(curr_player.hand[card_index])):  # card can be played on pile
                    self.pile_of_cards.add_card_to_stack(
                        curr_player.play_card(card_index))
                    if curr_player.last_card():
                        print("Mau!")
                    print("played card:", self.pile_of_cards.top())
                    break
                elif card_drawn:    # card was drawn and cannot be placed on the pile
                    print("No card has been played")
                    break
                else:           # card is not valid
                    print("Card cannot be played! Choose another card.")
            if curr_player.hand_is_empty():  # winning condition, players hand is empty
                print("Mau Mau!")
                self.score_count()
                break
            players_turn = (players_turn + 1) % self.amount_of_players
            input("next turn")

    @staticmethod
    def clear_screen():
        """clears terminal for every os"""
        os.system('clear') if sys.platform != "windows" else os.system('cls')
