"""Test file for the functions used in this game"""
import pytest
from unittest.mock import patch, mock_open
from Game import game_logic, player_input

from Game.game_logic import load_words, select_target_word, check_guess
from main import user_statistics, calculate_wins_losses, handle_guess

def test_load_words():
    """tests that the list of valid words matches the words in the txt file"""
    words = load_words('Words/words.txt')
    assert words == ['happy', 'sigma', 'bottle', 'phone']

def test_select_target_word():
    words = ['happy', 'sigma', 'bottle', 'phone']
    for _ in range(100000): #random range incase list of words is really long
        word = game_logic.select_target_word(words)
        assert word in words

def test_check_guess():
    """test to check if the symbols match up to the letters that are correct/wrong"""
    assert check_guess('word', 'word') == ['+', '+', '+', '+']
    assert check_guess('word', 'ward') == ['+', '-', '+', '+']
    assert check_guess('word', 'list') == ['-', '-', '-', '-']
    assert check_guess('word', 'owrt') == ['~', '~', '+', '-']

@patch('builtins.open', new_callable=mock_open, read_data="Date: 16/05/2023, Guesses: 2, Win/Lose: Win, Wins to date: 0, Losses to date: 0\n")
def test_calculate_wins_losses(mock_file):
    """Test to check if the calculate_wins_losses function identifies 'win' and adds 1 to wins"""
    wins, losses = calculate_wins_losses('Words/results.txt')
    assert wins == 1
    assert losses == 0

@patch('main.calculate_wins_losses', return_value=(0, 0))
@patch('builtins.open', new_callable=mock_open)
def test_user_statistics(mock_file, mock_calculate):
    """Test to check if the user_stats function writes to results.txt correctly"""
    wins, losses = user_statistics(1, True, 'Words/results.txt')
    mock_file.assert_called_once_with('Words/results.txt', 'a')
    mock_file().write.assert_called_once()
    assert wins == 1
    assert losses == 0
