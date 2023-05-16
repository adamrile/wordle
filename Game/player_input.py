"""Python script to collect the player's guess and print
messages corresponding to a win or loss"""

def ask_player_guess(guesses_left:int) -> str:
    """Function to ask the player for their guess"""
    print(f"{guesses_left} guesses left.")
    return input("Enter a five letter word: ").lower()

def print_guess_results(guess: str, results: str) -> str:
    """Function to get the result of the guess"""
    print(guess)
    print(''.join(results))

def print_end_message(won: bool, target_word:str) -> str:
    """Function to print the final win/loss message"""
    if won:
        print(f"Congratulations! The word was {target_word}.")
    else:
        print(f"You lost. The word was {target_word}.")
