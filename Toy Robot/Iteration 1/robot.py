
def move_in_square(size):
    """ Move forward size units. Turn right 90 degrees. Repeat 4 times. """

    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_in_rectangle(length, width):
    """ Move in rectangle of length * width.
    
    Move forward length units before turning right 90 degrees,
    move forward width units before turning right 90 degrees. Repeat twice.
    """
    
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_in_circle():
    """ Move forward then turn one degree to the right. Repeat 360 times. """

    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def square_dancing():
    """ Move 20 units forward before moving in a square. Repeat 3 times. """

    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward", 20)
        move_in_square(20)


def crop_circles():
    """ Move 20 units forward before moving in a circle. Repeat 4 times. """

    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        move_in_circle()


def move():
    """ Move the robot. """

    move_in_square(10)
    move_in_rectangle(20, 10)
    move_in_circle()
    square_dancing()
    crop_circles()


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
