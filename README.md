# Word Guessing Game

This is a command line version of the game "Wordle". The game selects a target word from a list of valid words and the player is given 5 attempts to guess the word.

## How to Play

Run the main.py script and follow the instructions on the screen. The player is asked to enter a guess. If the guess is not a valid word, the player is asked to try again. The player's guess is then checked against the target word and the result is printed on the screen. If the player guesses the word correctly, a win message is printed and the game ends. If not, the player is asked to guess again.

## Function Descriptions

- `user_statistics(guesses: int, win: bool, file_path: str) -> tuple[int, int]`: Writes the user statistics to a file in the /Words directory. If the game is won, the win count is incremented, otherwise the loss count is incremented.

- `calculate_wins_losses(file_path: str) -> tuple[int, int]`: Reads the wins and losses from a file in the /Words directory and returns them as a tuple.

- `handle_guess(target_word: str, valid_words: list, guesses_left: int) -> bool`: Handles the player's guess. If the guess is not a valid word, the player is asked to try again. If the guess is correct, a victory message is printed and True is returned. If the guess is incorrect, False is returned.

- `main()`: The main function that runs the game. It loads the valid words, selects a target word, and then enters a loop where the player is asked to guess the word. If the player guesses the word correctly, the win count is incremented and the game ends. If the player fails to guess the word after 5 attempts, the loss count is incremented and the game ends.

## Dependencies

This game requires the Game module, which contains the game_logic and player_input modules. Make sure these are present in the same directory as the main.py script.

## How to Run

Run the main.py script in Python 3. For example:

- `python3 main.py`

Enjoy the game!
