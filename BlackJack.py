from random import shuffle
import decimal

class Card():
    def __init__(self, value, suit, pip):
        self.value = value
        self.suit = suit
        self.pip = pip

    def __repr__(self):
        return f' {self.pip}{self.suit}'

    def show(self):
        if self.pip == "10":
            print(" ___________")
            print("|{}{}        |".format(self.pip, self.suit))
        else:
            print(" ___________")
            print("|{}{}         |".format(self.pip, self.suit))


class Deck():
    pips = [("A", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("J", 10), ("Q", 10), ("K", 10)] # refine
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self):
        super().__init__()
        self.deck = []
        for suit in self.suits:
            for pip, value in self.pips:
                new_card = Card(value=value, suit=suit, pip=pip)
                self.deck.append(new_card)

    def __str__(self):
        return self.deck

    def shuffle(self):
        shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def show(self):
        for card in self.deck:
            card.show()

class Hand():
    def __init__(self):
        super().__init__()
        self.cards = []

    def hit(self, deck):
        self.cards.append(deck.draw_card())

    def show(self):
        for card in self.cards:
            card.show()

    def get_value(self):
        hand_value = 0
        for card in self.cards:
            hand_value += card.value
        print(hand_value)



class DealerHand(Hand):

    def __init__(self):
        super().__init__()

    def show(self):
        for card in self.cards[:-1]:
            card.show()
        print(" ___________")
        print("|??         |")


class Player(Hand):

    def __init__(self):
        super().__init__()
        self.name = input("What's your name punk? ")
        while True:
            self.money = self.validator(input("How much do you have? ")) #  ok this is shit, nevermind
            if self.money > 0:
                break

    def validator(self, amount):
        try:
            return (decimal.Decimal(amount).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))
        except decimal.InvalidOperation:
            print("{}!? You're nuts or something?".format(amount))
            return 0


    def bet(self, amount):
        if self.validator(amount) <= self.balance:
            self.balance -= self.validator(amount)
            self.check()
