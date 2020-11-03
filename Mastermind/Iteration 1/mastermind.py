import random

def generate_code():
    """ Return a 4 digit code in a list, each digit is between 1 and 8. """

    code_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    code = []
    for i in range(4):
        digit_index = random.randint(1, len(code_range) - 1)
        digit = code_range[digit_index]
        code.append(digit)
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return ''.join(code)


def get_guess():
    """ Return user input for a guess as a string.
    
    Gets user input and only accepts a four digit code.
    Each digit has to be between a predefined range (1-8).
    """ 

    guess = input('Input 4 digit code: ')
    while guess.strip() == '' or len(guess) != 4 or not guess.isnumeric() or not check_in_range(guess):
        print('Please enter exactly 4 digits.')
        guess = input('Input 4 digit code: ')
    return guess


def check_in_range(guess):
    """ Return if guess only has digits in range of 1 - 8 or not. """

    code_range = ['1', '2', '3', '4', '5', '6', '7', '8']
    for elem in guess:
        if not elem in code_range:
            return False
    return True


def compare_guess(guess, answer, turns):
    """ Compare if guess is equal to answer or not.

    If so the function will return a tuple in the form:
    (True, turns). The true is used to indicate that the game should end.
    If guess != answer, turns will be decremented and the returned tuple
    will be in the form: (False, turns-1). 
    """

    finished = False
    compare_right_pos(guess, answer)
    compare_wrong_pos(guess, answer)
    if guess == answer:
        print('Congratulations! You are a codebreaker!')
        print('The code was: ' + guess)
        finished = True
    else:
        turns -= 1
        print('Turns left:', turns)
    return finished, turns


def compare_wrong_pos(guess, answer):
    """ Print the number of elements in answer that exist in guess. """

    num = 0
    for elem, index in zip(guess, answer):
        if elem in answer and not elem == index:
            num += 1
    print('Number of correct digits not in correct place:', num)


def compare_right_pos(guess, answer):
    """ Print the number of matching indeces in answer and guess. """

    num = 0
    for elem, index in zip(guess, answer):
        if elem in answer and elem == index:
            num += 1
    print('Number of correct digits in correct place:    ', num)


def run_game():
    """ Loops the game for 12 turns or until user guess is correct. """

    end_conditions = (False, 12)
    game_code = generate_code()
    while not end_conditions[0] == True and end_conditions[1] > 0:
        player_guess = get_guess()
        end_conditions = compare_guess(player_guess, game_code, end_conditions[1])


if __name__ == "__main__":
    run_game()
