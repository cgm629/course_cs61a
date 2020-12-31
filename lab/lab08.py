class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)

from classes import *
from cards import *

try:
    import readline
except ImportError:
    pass

###########
# Parsing #
###########

def card_parse(line, handsize):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    elif len(tokens) > 1:
        raise SyntaxError('Too many inputs')
    card_index = tokens.pop(0)
    if not card_index.isdigit():
        raise SyntaxError('Wrong type of input')
    card_index = int(card_index)
    if card_index >= handsize or card_index < 0:
        raise SyntaxError('Invalid card number')
    return card_index

def name_parse(line):
    if not line:
        raise SyntaxError('No command given')
    return line

########
# REPL #
########

def read_eval_print_loop():
	while True:
		try:
			line = input('What is your name?> ')
			name = name_parse(line)
			break
		except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
			print('\nSee you next game!')
			return
		except SyntaxError as e:
			print('ERROR:', e)
	p1 = Player(player_deck, name)
	p2 = Player(opponent_deck, 'Opponent')
	print(WELCOME_MESSAGE)
	duel = Game(p1, p2)
	draw = True
	while True:
		if duel.game_won() == 1:
			print(WIN_MESSAGE)
			return
		elif duel.game_won() == 2:
			print(LOSE_MESSAGE)
			return
		print()
		try:
			if draw:
				p1.draw()
				p2.draw()
			else:
				draw = True
			p1.display_hand()
			print('Please enter the number next to the card you would like to play this round.')
			line = input('card> ')
			card_index = card_parse(line, len(p1.hand))
			duel.play_round(p1.play(card_index), p2.play_random())
			duel.display_scores()
		except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
			print('\nGood game. Bye!')
			return
		except AssertionError: # Deck out
			if p1.deck.is_empty() and p2.deck.is_empty():
				print(TIE_MESSAGE)
				return
			elif p1.deck.is_empty():
				print(PLAYER_DECKOUT_MESSAGE)
				return
			else:
				print(OPPONENT_DECKOUT_MESSAGE)
				return
		except SyntaxError as e:
			print('ERROR:', e)
			draw = False

#################
# Configuration #
#################

WELCOME_MESSAGE = """
Welcome to Magic: The Lambda-ing!
Your code has taken on a mind of its own and has
challenged you to a game of cards! If you need a refresher
on the rules, check out the section on the lab page.
Let's get this duel started, shall we?
"""

WIN_MESSAGE = """
You have vanquished your foe in a duel!
Congratulations! You won this game of Magic: The Lambda-ing!
"""

LOSE_MESSAGE = """
You have been defeated by your foe in a duel!
I'm sorry, you lost this game of Magic: The Lambda-ing.
"""

TIE_MESSAGE = """
You and your opponent have no cards left in your decks!
You tied this game of Magic: The Lambda-ing. Who will win if you play again?
"""

PLAYER_DECKOUT_MESSAGE = """
You have no cards left in your deck!
I'm sorry, you lost this game of Magic: The Lambda-ing.
"""

OPPONENT_DECKOUT_MESSAGE = """
Your opponent has no cards left in their deck!
Congratulations! You won this game of Magic: The Lambda-ing!
"""

if __name__ == '__main__':
    read_eval_print_loop()
# All cards available in a standard deck.
from classes import *

#TAs
aaron = TACard('Baron Aaron', 2100, 1300)
albert = TACard('Al-bear', 1600, 1700)
aman = TACard('Aman', 1000, 2100)
cesar = TACard('Cesar, Sponsor of Good Vibes™', 1600, 1700)
chae = TACard('Chae', 1500, 1900)
danelle = TACard('Danelle Nachos', 2200, 1100)
derrick = TACard('EZ4ENCE', 1100, 2000)
isabelle = TACard('Isabelle', 1500, 1800)
jemmy = TACard('Jemmy', 1600, 1800)
lauren = TACard("Explorin' Lauren", 1200, 2200)
michelle = TACard('MICHELLE, De SOUs chef of ZA kingdom', 1500, 1800)
olivia  = TACard('shocked pikachu', 1900, 1500)
pavan = TACard('Pavan', 1400, 2000)
richard = TACard('Richard', 1500, 1900)
ryan = TACard('Ryan', 1500, 1800)
sean = TACard('Sean, Maker of Boba', 1700, 1500)
shide = TACard('ShidzZz of YeetzZz', 1700, 1500)

#Tutors
ada = TutorCard('Hu is Ada???', 2100, 1300)
aini = TutorCard('MacarAini and Cheese', 1800, 1500)
christine = TutorCard('Christine', 1500, 1700)
grant = TutorCard('Grant', 1100, 2100)
jennifer  = TutorCard('Jen, Head of Squirrels On Campus', 1600, 1700)
kaavya = TutorCard('Kaavya', 2200, 1200)
kaitlyn = TutorCard('Kaitlyn', 1300, 2000)
kevin = TutorCard('Kevin', 1500, 1900)
kunal = TutorCard('Kunal', 1500, 1500)
nancy = TutorCard('Banancy', 1500, 1700)
raghav = TutorCard('Raghav', 1400, 2000)
rahul_a = TutorCard('Rahul (disambiguation needed)', 2400, 1000)
rahul_d = TutorCard('Rahul', 1700, 1600)
rina = TutorCard('Rina', 1500, 1800)


# Insturctors
alex = InstructorCard('President Lieutenant Stennet for Senate', 2000, 4000)
tiffany = InstructorCard('Tall Tiff', 4000, 2000)
chris = InstructorCard('Chris, Caller of Men', 3000, 3000)

# A standard deck contains all standard cards.
standard_cards = [alex, tiffany, chris, aaron, albert, aman, cesar, chae, danelle, derrick, isabelle, jemmy, lauren, michelle, olivia , pavan, richard, ryan, sean, shide, ada, aini, christine, grant, jennifer , kaavya, kaitlyn, kevin, kunal, nancy, raghav, rahul_a, rahul_d, rina]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()

# Magic the Lambda-ing!

import random

class Card(object):
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        """
        Create a Card object with a name, attack,
        and defense.
        >>> staff_member = Card('staff', 400, 300)
        >>> staff_member.name
        'staff'
        >>> staff_member.attack
        400
        >>> staff_member.defense
        300
        >>> other_staff = Card('other', 300, 500)
        >>> other_staff.attack
        300
        >>> other_staff.defense
        500
        """
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, other_card):
        """
        Calculate power as:
        (player card's attack) - (opponent card's defense)/2
        where other_card is the opponent's card.
        >>> staff_member = Card('staff', 400, 300)
        >>> other_staff = Card('other', 300, 500)
        >>> staff_member.power(other_staff)
        150.0
        >>> other_staff.power(staff_member)
        150.0
        >>> third_card = Card('third', 200, 400)
        >>> staff_member.power(third_card)
        200.0
        >>> third_card.power(staff_member)
        50.0
        """
        return self.attack - other_card.defense / 2

    def effect(self, other_card, player, opponent):
        """
        Cards have no default effect.
        """
        pass

    def __repr__(self):
        """
        Returns a string which is a readable version of
        a card, in the form:
        <cardname>: <cardtype>, [<attack>, <defense>]
        """
        return '{}: {}, [{}, {}]'.format(self.name, self.cardtype, self.attack, self.defense)

    def copy(self):
        """
        Returns a copy of this card.
        """
        return Card(self.name, self.attack, self.defense)

class Player(object):
    def __init__(self, deck, name):
        """Initialize a Player object.
        A Player starts the game by drawing 5 cards from their deck. Each turn,
        a Player draws another card from the deck and chooses one to play.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> len(test_deck.cards)
        1
        >>> len(test_player.hand)
        5
        """
        self.deck = deck
        self.name = name
        self.hand = [deck.draw() for _ in range(5)]

    def draw(self):
        """Draw a card from the player's deck and add it to their hand.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> test_player.draw()
        >>> len(test_deck.cards)
        0
        >>> len(test_player.hand)
        6
        """
        assert not self.deck.is_empty(), 'Deck is empty!'
        self.hand.append(self.deck.draw())

    def play(self, card_index):
        """Remove and return a card from the player's hand at the given index.
        >>> from cards import *
        >>> test_player = Player(standard_deck, 'tester')
        >>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
        >>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
        >>> test_player.hand = [ta1, ta2, tutor1, tutor2]
        >>> test_player.play(0) is ta1 
        True
        >>> test_player.play(2) is tutor2 
        True
        >>> len(test_player.hand)
        2
        """
        return self.hand.pop(card_index)

    def display_hand(self):
        """
        Display the player's current hand to the user.
        """
        print('Your hand:')
        for card_index, displayed_card in zip(range(len(self.hand)),[str(card) for card in self.hand]):
            indent = ' '*(5 - len(str(card_index)))
            print(card_index, indent + displayed_card)

    def play_random(self):
        """
        Play a random card from hand.
        """
        return self.play(random.randrange(len(self.hand)))

######################
# Optional Questions #
######################

class TutorCard(Card):
    cardtype = 'Tutor'

    def effect(self, other_card, player, opponent):
        """
        Discard the first 3 cards in the opponent's hand and have
        them draw the same number of cards from their deck.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> other_card = Card('other', 500, 500)
        >>> tutor_test = TutorCard('Tutor', 500, 500)
        >>> initial_deck_length = len(player2.deck.cards)
        >>> tutor_test.effect(other_card, player1, player2)
        p2 discarded and re-drew 3 cards!
        >>> len(player2.hand)
        5
        >>> len(player2.deck.cards) == initial_deck_length - 3
        True
        """
        [opponent.hand.pop(0) for _ in range(3)]
        opponent.hand += [opponent.deck.draw() for _ in range(3)]
        #Uncomment the line below when you've finished implementing this method!
        print('{} discarded and re-drew 3 cards!'.format(opponent.name))

    def copy(self):
        """
        Create a copy of this card.
        """
        return TutorCard(self.name, self.attack, self.defense)

class TACard(Card):
    cardtype = 'TA'

    def effect(self, other_card, player, opponent):
        """
        Swap the attack and defense of an opponent's card.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> other_card = Card('other', 300, 600)
        >>> ta_test = TACard('TA', 500, 500)
        >>> ta_test.effect(other_card, player1, player2)
        >>> other_card.attack
        600
        >>> other_card.defense
        300
        """
        other_card.attack, other_card.defense = other_card.defense, other_card.attack

    def copy(self):
        """
        Create a copy of this card.
        """
        return TACard(self.name, self.attack, self.defense)

class InstructorCard(Card):
    cardtype = 'Instructor'

    def effect(self, other_card, player, opponent):
        """
        Increase attack/defense of every card in the player's
        deck by 300 each, then adds a copy of the opponent's card
        to both the player's deck and to their hand.
        >>> test_card = Card('card', 300, 300)
        >>> instructor_test = InstructorCard('Instructor', 500, 500)
        >>> opponent_card = test_card.copy()
        >>> test_deck = Deck([test_card.copy() for _ in range(8)])
        >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
        >>> instructor_test.effect(opponent_card, player1, player2)
        p2's card added to p1's hand and deck!
        >>> [(card.attack, card.defense) for card in player1.deck.cards]
        [(600, 600), (600, 600), (600, 600), (300, 300)]
        >>> len(player1.hand)
        6
        >>> opponent_card.attack
        300
        >>> opponent_card.defense
        300
        """
        for card in player.deck.cards:
            card.attack += 300
            card.defense += 300
        player.hand.append(other_card.copy())
        player.deck.cards.append(other_card.copy())
        #Uncomment the line below when you've finished implementing this method!
        print('{}\'s card added to {}\'s hand and deck!'.format(opponent.name, player.name))

    def copy(self):
        """
        Create a copy of this card.
        """
        return InstructorCard(self.name, self.attack, self.defense)

# class ProfessorCard(Card):
#     cardtype = 'Professor'

#     def effect(self, other_card, player, opponent):
#         """
#         Adds the attack and defense of the opponent's card to
#         all cards in the player's deck, then removes all cards
#         in the opponent's deck that share an attack or defense
#         stat with the opponent's card.
#         >>> test_card = Card('card', 300, 300)
#         >>> professor_test = ProfessorCard('Professor', 500, 500)
#         >>> opponent_card = test_card.copy()
#         >>> test_deck = Deck([test_card.copy() for _ in range(8)])
#         >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
#         >>> professor_test.effect(opponent_card, player1, player2)
#         3 cards were discarded from p2's deck!
#         >>> [(card.attack, card.defense) for card in player1.deck.cards]
#         [(600, 600), (600, 600), (600, 600)]
#         >>> len(player2.deck.cards)
#         0
#         """
#         orig_opponent_deck_length = len(opponent.deck.cards)
#         # BEGIN SOLUTION
#         for card in player.deck.cards:
#             card.attack += other_card.attack
#             card.defense += other_card.defense
#         for card in opponent.deck.cards[:]:
#             if card.attack == other_card.attack or card.defense == other_card.defense:
#                 opponent.deck.cards.remove(card)
#         # END SOLUTION
#         discarded = orig_opponent_deck_length - len(opponent.deck.cards)
#         if discarded:
#             #Uncomment the line below when you've finished implementing this method!
#             #print('{} cards were discarded from {}\'s deck!'.format(discarded, opponent.name))
#             return

#     def copy(self):
#         return ProfessorCard(self.name, self.attack, self.defense)


########################################
# Do not edit anything below this line #
########################################

class Deck(object):
    def __init__(self, cards):
        """
        With a list of cards as input, create a deck.
        This deck should keep track of the cards it contains, and
        we should be able to draw from the deck, taking a random
        card out of it.
        """
        self.cards = cards

    def draw(self):
        """
        Draw a random card and remove it from the deck.
        """
        assert self.cards, 'The deck is empty!'
        rand_index = random.randrange(len(self.cards))
        return self.cards.pop(rand_index)

    def is_empty(self):
        return len(self.cards) == 0

    def copy(self):
        """
        Create a copy of this deck.
        """
        return Deck([card.copy() for card in self.cards])

class Game(object):

    win_score = 8

    def __init__(self, player1, player2):
        """
        Initialize a game of <REPLACE NAME>.
        """
        self.player1, self.player2 = player1, player2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, p1_card, p2_card):
        """
        After each player picks a card, play them against
        each other.
        """
        p1_card.effect(p2_card, self.player1, self.player2)
        p2_card.effect(p1_card, self.player2, self.player1)
        p1_power = p1_card.power(p2_card)
        p2_power = p2_card.power(p1_card)
        if p1_power > p2_power:
            # Player 1 wins the round.
            self.p1_score += 1
            result = 'won'
        elif p2_power > p1_power:
            # Player 2 wins the round.
            self.p2_score += 1
            result = 'lost'
        else:
            # This round is a draw.
            result = 'tied'
        # Display results to user.
        print('You {} this round!'.format(result))
        print('{}\'s card: {}; Power: {}'.format(self.player1.name, p1_card, p1_power))
        print('Opponent\'s card: {}; Power: {}'.format(p2_card, p2_power))


    def game_won(self):
        """
        Check if the game is won and, if so,
        which player won.
        """
        if self.p1_score < self.win_score and self.p2_score < self.win_score:
            return 0
        return 1 if self.p1_score > self.p2_score else 2

    def display_scores(self):
        """
        Display players' scores to the user.
        """
        print('{}\'s score: {}'.format(self.player1.name, self.p1_score))
        print('Opponent\'s score: {}'.format(self.p2_score))
