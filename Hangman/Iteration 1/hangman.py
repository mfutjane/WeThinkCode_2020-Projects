import random

def read_file(file_name):
    """ Return a list including every line in file_name. """
    
    return open(file_name).readlines()

def select_random_word(words):
    """ Return a random word from words. """

    word_index = random.randint(0, len(words))
    letter_index = random.randint(0, len(words[word_index].strip()))
    print(f"Guess the word: {words[word_index][:letter_index] + '_' + words[word_index][letter_index+1:]}")
    return words[word_index].strip()


def get_user_input():
    """ Get user input and return a lowercase version. """

    user_guess = input('Guess the missing letter: ').lower()
    return user_guess.strip()


def run_game(file_name):
    """ Run one cycle of the game. Print word at the end. 
        
    A cycle consists of:
    - Reading the file passed in as file_name
    - Getting a random word from the list in the file
    - Printing a clue and allowing the player a guess.
    """
    word_list = read_file(file_name)
    selected_word = select_random_word(word_list)
    given_input = get_user_input()
    
    print(f'The word was: {selected_word}\n')

if __name__ == "__main__":
    run_game('short_words.txt')

