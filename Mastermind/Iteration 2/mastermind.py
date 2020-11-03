import random

def generate_code():
    """ Return 4 digit list with ints between 1 and 8. """

    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code


def in_range(potential_answer):
    """ Return if potential answer has 4 digits between 1-8 or not. """

    for elem in potential_answer:
        if not int(elem) in range(1, 9):
            return False
    return True


def get_guess():
    """ Get guess from the user until they input a 4 digit guess. """

    answer = input("Input 4 digit code: ")
    if len(answer) != 4 or not answer.isnumeric() or not in_range(answer):
        print("Please enter exactly 4 digits.")
        answer = get_guess()
    return answer


def compare_guess(answer, code):
    """ Compare answer to code at every index.

    If any guessed digit matches position and number, increment
    correct digits in correct place. If only the digit is correct
    but not the position, increment the correct digits not
    in the correct place. Print both.
    """

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))


def check_if_winner(answer, code):
    """ Return if answer matches code or not. """

    for x, y in zip(answer, code):
        if not int(x) == y:
            return False
    print('Congratulations! You are a codebreaker!')
    return True        


def max_guesses_check(turns, maximum):
    """ Return if user has ran out of guesses or not. """

    if turns == maximum:
        print('Sorry you are out of guesses')
        return True
    return False


def game_loop():
    """ Game loop. 
    
    As long as the player has not won or run out of turns:
    Get a guess. Compare that guess to the code. Add a turn.
    If the player is right or has run out of turns, end the loop,
    otherwise print how many turns are left.
    """

    correct = False
    turns = 0
    code = generate_code()
    while not correct and turns < 12:
        answer = get_guess()
        compare_guess(answer, code)
        turns += 1
        correct = check_if_winner(answer, code)
        if correct or max_guesses_check(turns, 12):
            break
        print('Turns left: '+str(12 - turns))
    print('The code was: '+str(code))


def run_game():
    game_loop()


if __name__ == "__main__":
    run_game()
