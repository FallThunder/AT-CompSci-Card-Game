from Utilities import modeSelect
from Utilities import dealCards
from Utilities import playRound
from Utilities import cardsCheck
import random
import os
import sys

def main():
    step = False
    manual = False

    # Clear the terminal
    os.system('clear')
    # Initialize the play again variable
    play_again = True

    print("Welcome to War!\n")

    # Select the way to step through the game
    mode = modeSelect()

    if mode == 'step':
        step = True
        input("Press enter to step through the games...\n")
        os.system('clear')

    elif mode == 'manual':
        manual = True
        input("Press enter to step through the games...\n")
        os.system('clear')

    # Create a score tracker for total games played and the number of wins for each player
    p1_score = 0
    p2_score = 0

    # Begin the game loop
    while play_again:
        print("Shuffling...\n")

        if manual:
            input("")

        # Deal the cards to the two players
        p1_hand, p2_hand = dealCards()

        print("Lets begin!\n")

        if manual or step:
            input("")

        # Initialize the round number
        round_num = 1

        # Begin the round loop, where the game is played until one player runs out of cards
        while len(p1_hand) > 0 and len(p2_hand) > 0:
            # Initialize the round variables
            won_round = False
            p1_played, p2_played = [], []

            print(f"Round {round_num}:")

            if manual or step:
                input("")

            # Begin the war loop, where the round is played until one player card trumps the others
            while not won_round:
                # Check if the players have cards to play
                if not cardsCheck(p1_hand, p2_hand):
                    # If one player is out of cards, the other player wins
                    if len(p1_hand) == 0:
                        print("Player 1 is out of cards! Player 2 wins!\n")
                        if manual or step:
                            input("")

                        p2_score += 1
                        break

                    else:
                        print("Player 2 is out of cards! Player 1 wins!\n")
                        if manual or step:
                            input("")

                        p1_score += 1
                        break

                else:
                    # Play the top card from each players hand
                    p1_played.append(p1_hand.pop(0))
                    p2_played.append(p2_hand.pop(0))

                print(f"Player 1 plays {p1_played[-1][0]} of {p1_played[-1][-1]}\n")

                if manual:
                    input("")

                print(f"Player 2 plays {p2_played[-1][0]} of {p2_played[-1][-1]}\n")

                if manual or step:
                    input("")

                # Determine the winner of the round
                result = playRound(p1_played[-1][0], p2_played[-1][0])

                # Handles the result of playRound
                if result == -1 or result == 1:
                    # Add the played cards to a temporary deck to be shuffled
                    added_hand = p1_played + p2_played
                    # Shuffle the cards
                    random.shuffle(added_hand)
                    # Add the shuffled cards to the winning players hand
                    if result == -1:
                        p1_hand.extend(added_hand)
                        print(f"Player 1 wins the round, with a new card count of {len(p1_hand)} cards!\n")

                        if manual:
                            input("")
                        won_round = True

                    else:
                        p2_hand.extend(added_hand)
                        print(f"Player 2 wins the round, with a new card count of {len(p2_hand)} cards!\n")

                        if manual or step:
                            input("")
                        won_round = True

                else:
                    continue

            # Increment the round number
            round_num += 1

        # Determine the winner of the game
        if len(p1_hand) > len(p2_hand):
            print(f"Player 1 wins the game in {round_num} rounds!\n")
            p1_score += 1

        else:
            print(f"Player 2 wins the game in {round_num} rounds!\n")
            p2_score += 1

        if manual or step:
            input("")

        # Print the current score
        if p1_score > p2_score:
            print(f"Player 1 leads with {p1_score} wins to Player 2 with {p2_score} wins.\n")

        elif p1_score < p2_score:
            print(f"Player 2 leads with {p2_score} wins to Player 1 with {p1_score} wins.\n")

        else:
            print(f"Player 1 and Player 2 are tied with {p1_score} wins each.\n")

        if manual or step:
            input("")

        print(f"{p1_score + p2_score} game(s) have been played.\n")
        
        if manual:
            input("")

        print("Would you like to play again? (return/n)")

        # Check if the user wants to play again
        if input() == 'n':
            sys.exit()

if __name__ == "__main__":
    main()