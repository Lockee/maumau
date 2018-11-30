"""pile of cards is a class which contains a list of cards objects"""

import card
import random


class StackOfCards:
    def __init__(self, is_pile, cards=[]):
        """initialise a deck or pile of cards,
        a deck when first created is filled with a normal skat game"""
        self.deck = []
        self.deck += cards
        if not is_pile:
            self.initalise_deck()
            self.shuffle()

    def draw(self):
        """returns the top card of the deck and removes it"""
        return self.deck.pop()

    def card_is_playable(self, card):
        """returns true if the top cards number or color
            matches the given card"""
        top_card = self.top()
        return top_card.is_same_number(card) or top_card.is_same_color(card)

    def add_card_to_deck(self, card):
        """adds a card object to the deck"""
        self.deck.append(card)

    def top(self):
        """returns last card object in deck"""
        return self.deck[-1]

    def pile_onto_deck(self, pile):
        """adds the deck of one stackofCards to its own"""
        self.deck += pile.deck

    def is_empty(self):
        """returns true if deck list is empty"""
        return len(self.deck) == 0

    def shuffle(self):
        """shuffles the deck list"""
        random.shuffle(self.deck)

    def show_deck(self):
        """pretty print deck list"""
        print(*self.deck, sep="\n")

    def initalise_deck(self):
        """adds every possible combination of cards in a skat game
            to the deck list"""
        numbers = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        houses = ["Hearts", "Spades", "Diamonds", "Clubs"]
        colors = ["red", "black"]
        self.deck = []
        i = 0
        for house in houses:
            for number in numbers:
                new_card = card.Card(number, colors[i], house)
                self.deck.append(new_card)
            i = (i+1) % 2

    def __len__(self):
        return len(self.deck)
