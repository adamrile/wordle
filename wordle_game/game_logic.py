import random
import os

def load_words(file_path: str) -> list:
    """Function to read and get all the words from
    the /Words directory"""
    with open(file_path, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]

def select_target_word(words:list) -> str:
    """Function to randomly choose a word from the
    list of words from load_words"""
    word_index = random.randint(0, len(words) - 1)
    return words[word_index]

def check_guess(target_word: str, guess:str) -> list:
    """Function to check the guess against the target word
    zip is used to iterate over corresponding characters in
    both words inside the zip"""
    result = []
    for i, j in zip(guess, target_word):
        if i == j:
            result.append('+')
        elif i in target_word:
            result.append('~')
        else:
            result.append('-')
    return result
