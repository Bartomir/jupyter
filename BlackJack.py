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
    pips = [("A", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7),
            ("8", 8), ("9", 9), ("10", 10), ("J", 10), ("Q", 10), ("K", 10)]
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self):
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
        self.cards = []

    def hit(self, deck):
        self.cards.append(deck.draw_card())

    def show(self):
        print("Your hand: ")
        for card in self.cards:
            card.show()
        print("Your hand value: {}".format(player.get_value()))

    def get_value(self):
        return validate(sum([card.value for card in self.cards]))

class Player(Hand):
    def __init__(self, name, money):
        super().__init__()
        self.name = name
        self.money = money

    def __str__(self):
        return f'{self.name}, {self.money}'

    def bet(self):
        self.bet = validate(input("How much you want to lose?: "))
        if validate(self.bet) <= self.money and validate(self.bet) != 0:
            self.money -= validate(self.bet)
        else:
            print("You can't do that!")

class DealerHand(Hand):
    def __init__(self):
        super().__init__()

    def show(self):
        print("Dealer's hand: ")
        for card in self.cards:
            card.show()
        print("Dealer's hand value: {}".format(dealer.get_value()))

    def show_hidden(self):
        print("Dealer's hand: ")
        for card in self.cards[:-1]:
            card.show()
        print(" ___________")
        print("|??         |")

def validate(amount):
    try:
        return (decimal.Decimal(amount))
    except decimal.InvalidOperation:
        pass

def show_table():
    player.show()
    print("Your hand value: {}".format(player.get_value()))
    dealer.show_hidden()

def first_draw():
    player.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    dealer.hit(deck)

def game_ongoing():
    if player.get_value() <= dealer.get_value() and dealer.get_value() <= 21:
        dealer.show()
        print("You've lost!!!")
    else:
        player.money += player.bet*2
        dealer.show()
        print("You lucky bastard!!!")
        print(player)

def game_end():
    if player.get_value() > 21:
        dealer.show()
        print("You've lost!!!")

name = input("What's your name punk? ")
while True:
    try:
        money = validate(input("How much do you have? ")) #  ok this is shit, nevermind
        if money < 10:
            print("{}!? That's not enough! Show me real money or get the fuck out! ".format(money))
        elif money % 10 != 0:
            money = money - (money % 10)
            print("Spare the change")
            break
        else:
            break
    except TypeError:
        print("What!? Are U nuts?")

player = Player(name, money)
deck = Deck()
dealer = DealerHand()
deck.shuffle()
player.bet()
first_draw()
show_table()

while True:
    choice = input("You hit or stay?: [h/s] ")
    if choice == 'h':
        player.hit(deck)
        player.show()
        game_end()
    elif choice == 's':
        player.show()
        break

while True:
    if player.get_value() > dealer.get_value() and dealer.get_value() <= 21:
        dealer.hit(deck)
        dealer.show_hidden()
    else:
        game_ongoing()
        break
