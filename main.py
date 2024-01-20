import random


class Deck:
    # Class attribue
    cards = []
    # Constructor - instance method by default
    def __init__(self):
        # When we initialize a new deck we default to the
        # class attribute value
        self.cards = Deck.cards
        for suit in Card.suits:
            for rank in Card.ranks:
                # Create a new card instance for each combination
                card = Card(suit, rank)
                # Add the card to the deck
                self.cards.append(card)
        return

    # Creating a static method to return a new, shuffled deck
    # This could be handy if you needed to start with a single, shuffled, deck
    @staticmethod
    def shuffle_deck():
        shuffle_suits = random.sample(Card.suits, len(Card.suits))
        shuffle_ranks = random.sample(Card.ranks, len(Card.ranks))
        for suit in shuffle_suits:
            for rank in shuffle_ranks:
                card = Card(suit, rank)
                # Update the class attribute
                Deck.cards.append(card)
        return Deck

    # Instance method to shuffle an existing deck
    # This would be helpful if you need to alter an existing deck
    def shuffle_current_deck(self):
        return random.sample(self.cards, len(self.cards))


class Card:
    # Class variables
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    # Constructor - instance method by default
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # String representation method - another instance method,
    # it's optional, but helpful
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Create a basic deck, no shuffling
deck1 = Deck()

print("\n---")
print("Standard Deck")
print("---")

for card in deck1.cards:
    print(card, end=',')

print("\n---")
print("Shuffled Deck")
print("---")

# Call the Class method shuffle_deck()
# to return a shuffled deck
deck2 = Deck.shuffle_deck()

# The Class method returns its own list of cards,
# independant of the cards attribute on the Deck class
for card in deck2.cards:
    print(card, end=',')

print("\n---")
print("Shuffle a Current Deck")
print("---")

# Call to an instance method shuffle_current_deck()
# this takes the deck from line 52 and returns a shuffled version
shuffle_my_deck = deck1.shuffle_current_deck()

for card in shuffle_my_deck:
    print(card, end=',')

