import random

def modeSelect():
    """
    Returns the mode of the game
    
    Parameters:
    - None
    
    Returns:
    - mode: string
    """
    mode = input("Would you like to have the game fully automated, through major steps or manually? (auto/step/manual)\n")
    if mode == "auto":
        return "auto"
    
    elif mode == "step":
        return "step"
    
    elif mode == "manual":
        return "manual"
    
    else:
        print("Invalid input, please try again.\n")
        modeSelect()

def dealCards():
    """
    Returns two lists of 26 tuples representing a deck of cards
    
    Parameters:
    - None
    
    Returns:
    - p1_hand: list of 26 tuples
    - p2_hand: list of 26 tuples
    """
    # Define the cards in a deck
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # Define the suites in a deck
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    # Create a deck of cards
    deck = [(rank, suit) for rank in ranks for suit in suits]

    # Initialize the hands for the two players
    p1_hand = []
    p2_hand = []

    # Shuffle the deck using the random module
    random.shuffle(deck)

    # Deal the cards to the two players
    p1_hand = deck[:26]
    p2_hand = deck[26:]

    # Return the hands
    return p1_hand, p2_hand

def playRound(p1_card, p2_card):
    """
    Returns the result of a round of war
    
    Parameters:
    - p1_card: string
    - p2_card: string
    
    Returns:
    - -1: if player 1 wins
    - 1: if player 2 wins
    - None: if the round is a tie
    """
    # Define the ranks of the cards
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Compare the ranks of the cards
    if ranks.index(p1_card) > ranks.index(p2_card):
        return -1
    
    elif ranks.index(p1_card) < ranks.index(p2_card):
        return 1

def cardsCheck(p1_hand, p2_hand):
    """
    Returns True if both players have cards to play
    
    Parameters:
    - p1_hand: list of tuples
    - p2_hand: list of tuples
    
    Returns:
    - True: if both players have cards to play
    - False: if one or both players are out of cards
    """
    # Check if the players have cards to play
    if len(p1_hand) == 0 or len(p2_hand) == 0:
        return False
    else:
        return True