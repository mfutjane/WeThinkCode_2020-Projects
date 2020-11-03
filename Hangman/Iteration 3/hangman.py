import random
import os
from sys import argv

def figures(wrong_attempts):
    """ Prints the correct frame for hangman depending on wrong attempts made.
    
       figures(2):
       
        /----
        |   0
        |
        |
        |
        _______
    """

    figure = ['/----\n|\n|\n|\n|\n_______',
                '/----\n|   0\n|\n|\n|\n_______',
                '/----\n|   0\n|  /|\\\n|\n|\n_______',
                '/----\n|   0\n|  /|\\\n|   |\n|\n_______',
                '/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______']
    print(figure[wrong_attempts - 1])

    
def read_file(file_name):
    """ Read file_name, return all the lines in a list. """

    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    """ Get a guess from the user and return it. """

    return input('Guess the missing letter: ')


def ask_file_name():
    """ Gets a file name from the user and returns it.

    If there is a single command line argument, try to use that as the file name.
    Otherwise ask the user for input. Should any of these not be a valid file,
    set the file name to short_words.txt.
    """

    if (len(argv) != 2):
        file_name = input("Words file? [leave empty to use short_words.txt] : ")
    else:
        file_name = argv[1]

    if not file_name or os.path.isfile(file_name) != True:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    """ Select a random word from words. Return the word. """

    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


def random_fill_word(word):
    """ Return word with one letter revealed and '_' elsewhere. """

    r = len(word)
    index_options = list(range(r))
    while len(index_options) > 1:
        index_option = random.randint(0, len(index_options) - 1)
        char_index = index_options[index_option]
        if not word[char_index] == '_':
            word = word.replace(word[char_index], '_', 1)
        del index_options[index_option]
    return word


def is_missing_char(original_word, answer_word, char):
    """ Return if char is in original word and hidden in answer word.
    
    Compare char to the original word, if it exists
    check if it has not been filled in inside answer. 
    If so, return true.
    """

    for elem in range(len(original_word)):
        if original_word[elem] == char and answer_word[elem] == '_':
            return True       
    return False


def fill_in_char(original_word, answer_word, char):
    """ Return updated answer word with char in correct place.
    
    Compare char to the original word, if it exists
    check if it has not been filled in inside answer. 
    If so, return the answer word with the char filled in.
    """

    for elem in range(len(original_word)):
        if original_word[elem] == char and answer_word[elem] == '_':
            return answer_word[:elem] + char + answer_word[elem + 1:]
    return answer_word


def do_correct_answer(original_word, answer, guess):
    """ Place guess in correct place, return updated answer. """

    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


def do_wrong_answer(answer, number_guesses):
    """ Print the number of guesses left and draw a hangman figure. """

    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


def draw_figure(number_guesses):
    """ Draw the figure stored at 5 - number of guesses taken. """

    figures(5 - number_guesses)


def end_game(player_input):
    """ Return if player input is exit/quit or not. """

    if player_input.lower() in ['exit', 'quit']:
        print('Bye!')
        return True
    return False


def run_game_loop(word, answer):
    """ Loop the game until the user is correct, quits, or runs out of guesses.
    
    The loop is:
    - Get a guess
    - Check if the user wants to quit, do so if they entered exit/quit
    - Check if the guess is correct and update answer if it is.
    If the guess is wrong, decrement num of guesses and print a figure
    """

    print("Guess the word: "+answer)
    guesses = 5
    while answer.count('_') > 0 and guesses > 0:
        guess = get_user_input()
        if end_game(guess):
            break

        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            guesses -= 1
            do_wrong_answer(answer, guesses)

    if guesses == 0:
        print('Sorry, you are out of guesses. The word was: ' + word)


if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

