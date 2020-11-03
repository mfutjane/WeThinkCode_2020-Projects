
def get_persistent_input(output_str):
    """ Ask the user for input. Return lowercase version. """
 
    user_input = ''
    while user_input.strip() == '':
        user_input = input(output_str).strip()
    return user_input.lower()


def get_shape():
    """ Get the user's preference of a shape. 
    
    Return none if shape does not exist.
    Otherwise return input in lowercase. 
    Defined shapes: pyramid, square, triangle, diamond.
    """

    user_shape = get_persistent_input("Shape?: ")
    if user_shape.lower() in ["pyramid", "square", "triangle", "diamond"]:
        return user_shape.lower()
    return None


def get_height():
    """ Get a user defined height. 
    
    If the height is not between 1 and 80,
    or non-integer is entered, ask again until input is valid.
    Return height as an integer.
    """

    while True:
        try:
            height = get_persistent_input("Height?: ")
            height = int(height) #will raise exception if height is not a num
            if height in range(1, 81):
                return height
        except:
            pass  


def get_outline():
    """ Get whether or not the user wants a shape printed in outline mode.
    
    Y means yes and N means no.
    Input starting with these letters will return true for y or false for no.
    Anything else will return none.
    """

    mode = get_persistent_input("Outline only? (y/n): ")
    options = {'y': True, 'n': False}
    if mode[0] in options:
        return options[mode[0]]
    return None


def draw_pyramid(height, outline):
    """ Print a pyramid of height rows. Print only the edge if outline is true. """

    if not outline:
        for line in range(1, height + 1):
            print_line(height-line, '*', 2*line-1)
    else:
        print(' '*(height-1) + '*')
        for line in range(1, height - 1):
            print_line(height-line-1, ' ', 2*line-1, pre_mid='*', end='*')
        print('*'*(2*height-1))


def draw_diamond(height, outline):
    """ Print a pyramid of 2*height-1 rows. Print the edge only if outline is true. """

    if not outline:
        for line in range(1, height + 1):
            print_line(height-line, '*', 2*line-1)
        for line in range(1, height):
            print_line(line, '*', 2*(height-line)-1)
    else:
        print(' '*(height-1) + '*')
        for line in range(1, height-1):
            print_line(height-line - 1, ' ', 2*line-1, pre_mid='*', end='*')
        for line in range(1, height):
            print_line(line - 1, ' ', 2*(height-line)-1, pre_mid='*', end='*')
        print(' '*(height-1) + '*')


def draw_square(height, outline):
    """ Print a square of height rows. If outline is true, print only the edge. """

    if not outline:
        for line in range(1, height + 1):
            print('*'*height)
    else:
        print('*'*height)
        for line in range(1, height -1):
            print_line(0, ' ', height-2, pre_mid='*', end='*')
        print('*'*height)          


def draw_triangle(height, outline):
    """ Print a triangle of height rows. If outline is true, print only the edge. """

    if not outline:
        for line_count in range(1, height + 1):
            print_line(0, '*', line_count)
    else:
        print('*')
        for line in range(0, height-2):
            print_line(0, ' ', line, pre_mid='*', end='*')
        print('*'*height)


def print_line(pre_spaces, middle, num_mid, pre_mid='', end=''):
    """ Print pre_spaces + pre_mid + middle*num_mid + end.
        
        print_line(5, '#', 3) will print '     ###'
        print_line(2, '#', 3, @) will print '  @###'
        print_line(0, '#', 3, @, @) will print '@###@' """

    print(' '*pre_spaces + pre_mid + middle*num_mid + end)


def draw(shape, height, outline):
    """ Call shape function and draw depending on outline definition. """

    if not outline == None:
        functions = {'pyramid': draw_pyramid,
                     'triangle': draw_triangle,
                     'square': draw_square,
                     'diamond': draw_diamond}
        functions[shape](height, outline)        


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

