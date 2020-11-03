import random

def create_code():
    """ Return 4 digit list with numbers between 1 and 8. """

    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code


def show_instructions():
    """ Print instructions. """

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(correct_digit_pos, correct_digit):
    """ Print correct_digit_pos and correct_digit. """

    if [type(correct_digit_pos), type(correct_digit)] != [int, int]:
        raise ValueError('Correct digit pos and correct digit should be numbers')

    print('Number of correct digits in correct place:     ' + str(correct_digit_pos))
    print('Number of correct digits not in correct place: ' + str(correct_digit))


def get_guess():
    """ Get 4 digit code guess from user. """ 

    answer = input("Input 4 digit code: ")
    while len(answer) != 4 or not answer.isnumeric():
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    if not in_range(answer):
        print("Please enter exactly 4 digits.")
        answer = get_guess()
    return answer


def in_range(guess):
    """ Return if guess only has digits between 1 and 8 or not. """

    for elem in guess:
        if not int(elem) in range(1, 9):
            return False
    return True


def take_turn(code):
    """ Handle the logic of taking a turn.
    
    This includes:
    Get answer from user.
    Check if answer is valid.
    Check correctness of answer.
    """
    if type(code) != list:
        raise ValueError('Code should be a list or string')
    
    if [type(x) for x in code] != [int, int, int, int]:
        raise ValueError('Code should only contain four integers')

    answer = get_guess()

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    return (correct_digits_and_position, correct_digits_only)


def show_code(code):
    """ Print code to user. """

    if type(code) != list:
        raise ValueError('Code should be a list')

    print('The code was: '+str(code))


def check_correctness(correct_digits_and_position, turns):
    """ Return if correct digits is 4. Print turns-1 otherwise."""

    if [type(correct_digits_and_position), type(turns)] != [int, int]:
        raise ValueError('Correct digit pos and correct digit should be numbers')

    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        return False


def run_game():
    """Main function for running the game"""

    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        guess_accuracy = take_turn(code)
        show_results(guess_accuracy[0], guess_accuracy[1])
        turns += 1
        correct = check_correctness(guess_accuracy[0], turns)

    show_code(code)


if __name__ == "__main__":
    run_game()
