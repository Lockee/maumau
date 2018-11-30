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
        self.amount_of_players = 0
        self.players = []
        self.turn = -1
        self.curr_player = None
        self.card_was_drawn = False
        self.card_index = -1

    def name_players(self):
        """gives every player a name, if no name is given the standard name
           PlayerX will be given"""
        self.players = []
        for i in range(self.amount_of_players):
            player_name = input("Please state your name player"+str(i+1)+": ")
            if player_name == "":  # no name given
                player_name = "Player" + str(i+1)   
            new_player = player.Player(player_name)
            self.players.append(new_player)

    def set_amount_of_players(self):
        """asks how many players are playing, can be between 2 and 4 players"""
        while True:
            amount_of_players = input("How many players are playing(2-4): ")
            if amount_of_players.isdigit() and 2 <= int(amount_of_players) <= 4:
                return int(amount_of_players)
            else:
                print("the number has to be between 2 and 4")

    def deal_cards_to_players(self):
        """Asks how many cards should the player start with and then distributes this
           amount of cards to the players"""
        amount_of_cards = 0
        while True:
            amount = input("How many cards should the players have at the start(3-5)?: ")
            if amount.isdigit() and 2 < int(amount) <= 5:
                amount_of_cards = int(amount)
                break
            else:
                print("Please enter a number between 3 and 5") 
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

    def rule_card_seven(self):
        """ TODO: Add rule for a seven"""
        pass

    def rule_card_eight(self):
        """ TODO: Add rule for a eight"""
        pass

    def rule_card_jack(self):
        """ TODO: Add rule for a jack"""
        pass

    def score_count(self):
        """adds a score to the players based on their cards left:
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
        """Initiates the next turn for the game"""
        self.clear_screen()
        self.reshuffle_deck()
        self.turn = (self.turn + 1) % self.amount_of_players
        self.curr_player = self.players[self.turn]
        self.card_was_drawn = False

    def reshuffle_deck(self):
        """if the deck is empty, the pile, without the open card,
           will be reshuffled into the deck"""
        if self.deck_of_cards.is_empty():
                self.add_pile_to_deck()
                self.deck_of_cards.shuffle()

    def info_prints(self):
        """prints some statistics which would be visible in the real card game,
           like the amount of cards in the other players hand and it's own cards"""
        print("Amount of cards in deck left:", len(self.deck_of_cards))
        print("Amount of cards on pile:", len(self.pile_of_cards))
        top_card = self.pile_of_cards.top()
        for player in self.players:
            if player is self.curr_player:
                continue
            print("Amount of cards in", player.name + "s hand:", len(player))
        print("===Top of Pile===")
        print(top_card)
        print("=================")
        print("it's", self.curr_player.name + "s", "turn.\n")
        print(self.curr_player, "d. Draw a Card", sep="")

    def player_chooses_option(self):
        """player input, asks if he/she wants to play or to draw a card"""
        while True:  # run as long as input is invalid
            card_index = input("Which card do you want to play?: ")
            if card_index.isdigit():
                self.card_index = int(card_index) - 1
                if self.card_index >= len(self.curr_player) or self.card_index < 0:
                    print("Please state a valid option.")
                    continue
                if not self.pile_of_cards.card_is_playable(self.curr_player.hand[self.card_index]):
                    print("Card is cannot be played, choose another card!")
                    continue
            elif card_index.lower() == "d":
                self.card_was_drawn = True
            else:
                print("Invalid input, try again")
                continue
            break

    def evaluate_option(self):
        """a card will be drawn, card_was_drawn evaluates to True,
           if possible the player gets the choice to play it right away,
           otherwise the player plays the card with the index of card_index"""
        if self.card_was_drawn:
            drawn_card = self.deck_of_cards.draw()
            print(drawn_card, "has been drawn.")
            if(self.pile_of_cards.card_is_playable(drawn_card)):
                play = ""
                while play != "y" and play != "n":
                    play = input("do you want to play it? (y)es or (n)o: ").lower()
                    if play == "y":
                        self.pile_of_cards.add_card_to_deck(drawn_card)
                    elif play == "n":
                        print(drawn_card, "will be added to your hand")
                        self.curr_player.add_card_to_hand(drawn_card)
                        print("No card has been played")
                        return
                    else:
                        print("please enter a valid option")
        else:
            self.pile_of_cards.add_card_to_deck(
                        self.curr_player.play_card(self.card_index))
            if self.curr_player.last_card():
                print("Mau!")
        print("played card:", self.pile_of_cards.top())

    def run(self):
        """Starts the game"""
        self.amount_of_players = self.set_amount_of_players()
        self.name_players()
        self.deal_cards_to_players()
        self.pile_of_cards.add_card_to_deck(self.deck_of_cards.draw())  # first open card
        while True:  # game loop
            self.next_turn()
            self.info_prints()
            self.player_chooses_option()
            self.evaluate_option()
            if self.curr_player.hand_is_empty():  # winning condition, players hand is empty
                print("Mau Mau!")
                self.score_count()
                break
            input("next turn!")

    @staticmethod
    def clear_screen():
        """clears terminal for every os"""
        os.system('clear') if sys.platform != "windows" else os.system('cls')