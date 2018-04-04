from random import shuffle
from decimal import Decimal

class Deck():

    pips = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self):
        self.deck = []
        for self.suit in Deck.suits:
            for self.pip in Deck.pips:
                card = (self.pip, self.suit)
                self.deck.append(card)
        #print(self.deck)

    def print_deck(self):
        print(self.deck)

    def shuffle(self):
        shuffle(self.deck)
        print(self.deck)

    def draw_card(self):
        return self.deck.pop()

class Hand():

    def __init__(self):
        self.cards = []

    def hit(self, deck):
        self.cards.append(deck.draw_card())
        print(self.cards)

    def show_card(self):
        if self.card[0] == "10":
            print(" ___________")
            print("|{}{}        |".format(self.card[0], self.card[1]))
        else:
            print(" ___________")
            print("|{}{}         |".format(self.card[0], self.card[1]))

    def show_hand(self):
        for self.card in self.cards:
            self.show_card()


    def hand_value(self):
        self.value = []
        for self.card in self.cards:
            print(self.card[0])
            if self.card[0] in ["J", "Q", "K"]:  # this will need to be refined
                self.value.append(10)
            elif self.card[0] == "A":
                self.value.append(11)
            else:
                self.value.append(int(self.card[0]))
        print(self.value)
        hand_value = sum(self.value)
        print(hand_value)

class Dealer_hand(Hand):

    def __init__(self):
        Hand.__init__(self)

    def show_hidden(self):  # needs refinement
        for self.card in self.cards:
            if self.card == (self.cards[-1]):
                print(" ___________")
                print("|??         |")
            else:
                self.show_card()
