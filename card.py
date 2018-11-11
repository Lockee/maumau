class Card():
    def __init__(self, num, color, house):
        self.num = num
        self.color = color
        self.house = house

    def is_same_number(self, other):
        return self.num == other.num

    def is_same_color(self, other):
        return self.color == other.color

    def __str__(self):
        return self.num + " of " + self.house + " | " + self.color
