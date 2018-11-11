import card
import random


class Deck:
    def __init__(self, is_stack, cards=[]):
        self.deck = []
        self.deck += cards
        if not is_stack:
            self.initalise_deck()
            self.shuffle()

    def draw(self):
        return self.deck.pop()

    def card_is_playable(self, card):
        top_card = self.top()
        return top_card.is_same_number(card) or top_card.is_same_color(card)

    def add_card_to_stack(self, card):
        self.deck.append(card)

    def top(self):
        return self.deck[-1]

    def add_stack_to_deck(self, stack):
        self.deck += stack.deck

    def is_empty(self):
        return len(self.deck) == 0

    def shuffle(self):
        random.shuffle(self.deck)

    def show_deck(self):
        print(*self.deck, sep="\n")

    def initalise_deck(self):
        numbers = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        houses = ["Hearts", "Spades", "Diamonds", "Clubs"]
        colors = ["red", "black"]
        i = 0
        for house in houses:
            for number in numbers:
                new_card = card.Card(number, colors[i], house)
                self.deck.append(new_card)
            i = (i+1) % 2

    def __len__(self):
        return len(self.deck)
