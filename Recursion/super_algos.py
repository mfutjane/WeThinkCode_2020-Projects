def is_of_type(elements, type):
    """ Return true if everything in elements is of type. False otherwise. """
    
    if not elements:
        return False

    for x in elements:
        if not isinstance(x, type):
            return False
    return True


def find_min(elements):
    """ Return the smallest value in elements. """

    if type(elements) is not list:
        raise ValueError('Elements should only be a list.')

    if not is_of_type(elements, int):
        return -1

    if len(elements) == 1:
        return elements[0]

    first_elem = elements.pop()
    next_elem = find_min(elements)
    return first_elem if first_elem < next_elem else next_elem 

def sum_all(elements):
    """ Return the sum of all values in elements. """

    if type(elements) is not list:
        raise ValueError('Elements should only be a list.')

    if not is_of_type(elements, int):
        return -1

    if len(elements) == 1:
        return elements[0]

    return elements.pop() + sum_all(elements)


def find_possible_strings(character_set, n):
    """ Return all possible string combinations of character_set of length n. """

    my_set = []

    if type(character_set) is not list:
        raise ValueError('Char set should only be a list.')

    if type(n) is not int:
        raise ValueError('N should only be an integer.')

    if n == 1:
        return character_set

    if n <= 0 or not is_of_type(character_set, str):
        return my_set

    for char in character_set:
        a_ = find_possible_strings(character_set, n-1)
        for elem in a_:
            my_set.append(char + elem)
    return my_set


if __name__ == "__main__":
    print(find_min([1,2,3,4,5,6]))
    print(sum_all([1,2,3,4,5,6]))
    print(find_possible_strings(['x', 'y'], 2))
