import random
import sys

#cards info
class Card:
    def __init__(self):
        self.card_points = {
            '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10,
            'A': [1, 11]
        }
        self.card_deck = {
            '2': 4,
            '3': 4,
            '4': 4,
            '5': 4,
            '6': 4,
            '7': 4,
            '8': 4,
            '9': 4,
            '10': 4,
            'J': 4,
            'K': 4,
            'A': 4
        }

    def draw_cards(self,person):
        card_release = None
        while card_release==None:
            draw = random.choice(list(self.card_deck.items()))
            if draw[1] == 0:
                continue
            else:
                card_release = draw[0]
                self.card_deck[card_release] -= 1
        person.calculate_score(card_release)
        return card_release

class Person:
    def __init__(self):
        self.cards = []
        self.points = 0
        self.stand = False
        self.bust = False
    def calculate_score(self,cards_get):
        self.cards.append(cards_get)
        score= 0
        cards_value=Card().card_points
        for card in self.cards:
            if score>= 11 and card == 'A':
                score+= 1
            else:
                score+=cards_value[card]
        self.points=score


#player's info and score
class Player(Person):
    def __init__(self):
        super().__init__()

    def status(self):
        if self.points>=21:
            self.bust=True

    def display(self):
        print("Player has:",*self.cards,'=',self.points)

    def action(self):
        command=input('Would you like to (H)it or (S)tand?')
        if command=='H':
            return 'H'
        elif command=='S':
            return 'S'

#dealer's info and score
class Dealer(Person):
    def __init__(self):
        super().__init__()

    def status(self):
        if 17<=self.points<21:
            self.stand=True
            print('Dealer stands')
        elif self.points>=21:
            self.bust=True

    def display(self,player):
        if player.stand==False:
            print('Dealer has',self.cards[0],'? = ?')
        else:
            print('Dealer has',*self.cards,'=',self.points)


#game
class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.cards=Card()

    def play_game(self):
        self.initialize()
        self.player_Turn()
        self.dealer_Turn()
        self.choose_winner()

    def initialize(self):
        player_card1= self.cards.draw_cards(self.player)
        player_card2 = self.cards.draw_cards(self.player)
        dealer_card1 = self.cards.draw_cards(self.dealer)
        dealer_card2 = self.cards.draw_cards(self.dealer)

    def player_Turn(self):
        while self.player.stand == False:
            self.dealer.display(self.player)
            self.player.display()
            self.player.status()
            if self.player.stand == True:
                self.choose_winner()
            self.user_Action()

    def dealer_Turn(self):
        while self.dealer.stand == False:
            self.dealer.display(self.player)
            self.dealer.status()
            if self.dealer.bust == True:
                self.choose_winner()
            elif self.dealer.stand == True:
                print("Dealer stands with:", *self.dealer.cards, "=", self.dealer.points)
                self.choose_winner()
            else:
                print("Dealer hits")
                self.cards.draw_cards(self.dealer)

    def user_Action(self):
        command = self.player.action()
        if command == 'H':
            drawn = self.cards.draw_cards(self.player)
        elif command == 'S':
            self.player.stand = True
            print("Player stands with:", *self.player.cards, "=", self.player.points)

    def choose_winner(self):
        if self.player.points==self.dealer.points:
            print('Even')
        elif self.player.points==21:
            print('Player wins!')
            print('Blackjack!')
        elif self.dealer.points==21:
            print('Dealer wins!')
            print('Blackjack!')
        elif self.player.points>21:
            print('Player busts with',self.player.points)
            print('Dealer wins')
        elif self.dealer.points>21:
            print('Dealer busts with', self.dealer.points)
            print('Player wins')
        elif self.player.points<self.dealer.points:
            print('Dealer wins!')
        elif self.player.points>self.dealer.points:
            print('Player Wins!')
            print(*self.player.cards,'=',self.player.points,"to Dealer's", *self.dealer.cards,'=',self.dealer.points)

        sys.exit()


if __name__=='__main__':
    Game().play_game()














