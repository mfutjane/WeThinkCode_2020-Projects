import sys
import turtle
from io import StringIO
from world.text import world

class World(world.World):

    def __init__(self, name):
        world.World.__init__(self, name)
        self.the_robot = turtle.Turtle()
        self.the_robot.degrees()
        self.draw_border()

    def draw_border(self):
        """ Draw the border and return the turtle to its start position. """

        #self.the_robot.hideturtle()
        self.the_robot.up()

        self.the_robot.goto(-101, 201)
        self.the_robot.down()
        
        self.the_robot.goto(-101, -201)
        self.the_robot.goto(101, -201)
        self.the_robot.goto(101, 201)
        self.the_robot.goto(-101, 201)

        self.the_robot.up()
        self.the_robot.goto(0,0)
        self.the_robot.down()

    def move_forward(self, distance):
        """ Run main move forward, then move the robot in turtle. """
        
        sys.stdout, temp = StringIO(), sys.stdout
        world.World.move_forward(self, distance)
        sys.stdout = temp
        self.the_robot.goto(self.position['x'], self.position['y'])

    def move_back(self, distance):
        """ Run main move back, then move the robot in turtle. """

        sys.stdout, temp = StringIO(), sys.stdout
        world.World.move_back(self, distance)
        sys.stdout = temp
        self.the_robot.goto(self.position['x'], self.position['y'])
    
    def turn_left(self, *args):
        """ Run main turn left, then turn the robot in turtle. """

        sys.stdout, temp = StringIO(), sys.stdout
        world.World.turn_left(self)
        sys.stdout = temp
        self.the_robot.left(90)
    
    def turn_right(self, *args):
        """ Run main turn right, then turn the robot in turtle. """

        sys.stdout, temp = StringIO(), sys.stdout
        world.World.turn_right(self)
        sys.stdout = temp
        self.the_robot.right(90)

    def sprint(self, distance):
        """ Run main sprint, then sprint the robot in turtle. """

        sys.stdout, temp = StringIO(), sys.stdout
        world.World.sprint(self, int(distance))
        sys.stdout = temp
        self.the_robot.goto(self.position['x'], self.position['y'])