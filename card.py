"""Card class which holds basic information about
the suit, number and color of a card"""


class Card():
    def __init__(self, num, color, suit):
        self.num = num
        self.color = color
        self.suit = suit

    def is_same_number(self, other):
        """compares if the numbers match"""
        return self.num == other.num

    def is_same_color(self, other):
        """compares if the colors match"""
        return self.color == other.color

    def __str__(self):
        """pretty print a card"""
        return self.num + " of " + self.suit + " | " + self.color
