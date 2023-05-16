"""Main script that brings all functions together runs the game"""
import datetime
from Game import game_logic, player_input

def user_statistics(guesses: int, win: bool, file_path: str) -> tuple[int, int]:
    """Function to write the user stats to results.txt in the /Words directory"""
    wins, losses = calculate_wins_losses(file_path)
    if win:
        wins += 1
    else:
        losses += 1

    with open(file_path, 'a') as file:
        file.write(f"Date: {datetime.datetime.now():%d/%m/%Y}, Guesses: {guesses}, Win/Lose: {'Win' if win else 'Lose'}, Wins to date: {wins}, Losses to date: {losses}\n")

    return wins, losses

def calculate_wins_losses(file_path: str) -> tuple[int, int]:
    """Function to add 1 to wins or losses respective of the result of the game"""
    wins = 0
    losses = 0

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            if 'Win' in line:
                wins += 1
            elif 'Lose' in line:
                losses += 1

    return wins, losses

def handle_guess(target_word: str, valid_words: list, guesses_left: int) -> bool:
    """Checks if the guess has any correct letters and if all letters are correct it prints
    a winning message otherwise it prints a losing message"""
    guess = player_input.ask_player_guess(guesses_left)
    if guess not in valid_words:
        print("Your guess is not in the list of valid words. Try again.")
        return False
    results = game_logic.check_guess(target_word, guess)
    player_input.print_guess_results(guess, results)
    if results == ['+'] * len(guess):
        player_input.print_end_message(True, target_word)
        return True
    return False

def main():
    """main function that shows the order that the functions need to run"""
    words = game_logic.load_words('Words/words.txt')
    target_word = game_logic.select_target_word(words)
    wins = 0
    losses = 0
    for guesses_left in range(5, 0, -1):
        if handle_guess(target_word, words, guesses_left):
            wins, losses = user_statistics(5 - guesses_left + 1, True, 'Words/results.txt')
            break
    else:
        player_input.print_end_message(False, target_word)
        wins, losses = user_statistics(5, False, 'Words/results.txt')

    print(f"Wins: {wins}, Losses: {losses}")

if __name__ == "__main__":
    main()
