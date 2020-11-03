import random
import re

def read_file(file_name):
    """ Read the file 'file_name' and return a list of its contents. """

    file = open(file_name,'r')
    word_list = list()

    for word in file:
        word_list.append(word.strip())
    file.close() #closing file to get rid of tracealloc error
    return word_list


def select_random_word(words):
    """ Select a random word from words, return the chosen word. """

    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word.strip()


def select_random_letter_from(word):
    """ Return random letter from word and its index.
    
    Replace random letter with an underscore
    and prompt user to guess that missing letter.
    """

    random_index = random.randint(0, len(word) - 1)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index


def get_user_input():
    """ Prompt user for a guess and return user's input. """
    
    return input('Guess the missing letter: ')


def show_answer(answer, selected_word, missing_letter_index):
    """ Compare answer to selected word at index and print response.
    
    Print what the selected word was, if the user guessed correctly
    congratulate them otherwise tell them they were wrong.
    """
    
    print("The word was: " + selected_word)
    if selected_word[missing_letter_index] == answer:
        print("Well done! You are awesome!")
    else:
        print("Wrong! Do better next time.")


def ask_file_name():
    """ Return a file name depending on user input.
    
    Ask the user for a file name. If an empty string or file that does not end
    in '.txt' is entered, return short-words. Otherwise return the user file.
    """

    file_name = input("Words file? [leave empty to use short_words.txt] :")
    if file_name.strip() == "" or re.search("\.txt$", file_name) == None:
        file_name = "short_words.txt"
    return file_name


def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

