import math
import import_helper
from sys import argv

what_to_get = 'maze.maze_generator' if ('simple_maze' in argv) else 'maze.obstacles'
obstacles = import_helper.dynamic_import(what_to_get)

class World(obstacles.Obstacles):

    def __init__(self, name):
        """ Setup the world and initiate obstacles. """
        obstacles.Obstacles.__init__(self)
        self.position = {'x':0, 'y':0}
        self.angle = 0

        self.maze_name = obstacles.__name__
        self.obstacle_met = False
        self.name = name

    def set_name(self, name):
        """ Set instance name. """

        self.name = name

    def move_forward(self, distance):
        """ Move the robot distance amount of steps forwards. """
        
        if not self.check_in_bounds(distance):
            self.cant_fly_off_cliff()
            self.update_position()
            return

        self.position['x'] += int(distance*math.sin(self.angle))
        self.position['y'] += int(distance*math.cos(self.angle))

        print(' > {} moved forward by {} steps.'.format(self.name, distance))
        self.update_position()

    def move_back(self, distance):
        """ Move the robot distance amount of steps backwards. """

        if not self.check_in_bounds(distance, direction=-1):
            self.cant_fly_off_cliff()
            self.update_position()
            return

        self.position['x'] -= int(distance*math.sin(self.angle))
        self.position['y'] -= int(distance*math.cos(self.angle))

        print(' > {} moved back by {} steps.'.format(self.name, distance)) 
        self.update_position()
        
    def turn_left(self, *args):
        """ Turn the robot left. """

        self.angle -= math.pi/2
        print(' > {} turned left.'.format(self.name))

        self.update_position()

    def turn_right(self, *args):
        """ Turn the robot right. """

        self.angle += math.pi/2
        print(' > {} turned right.'.format(self.name))

        self.update_position()

    def sprint(self, distance):
        """ Sprint the robot forward at a decreasing rate starting from distance steps. """

        total_steps = (distance**2 + distance)/2

        if not self.check_in_bounds(total_steps):
            self.cant_fly_off_cliff()
            return
        if distance == 0:
            self.update_position()
            return

        print(" > {} moved forward by {} steps.".format(self.name, distance))
        self.position['x'] += int(distance*math.sin(self.angle))
        self.position['y'] += int(distance*math.cos(self.angle))
        self.sprint(distance-1)

    def update_position(self):
        """ Print the robot's current position. """

        print(' > {} now at position ({},{}).'.format(self.name, int(self.position['x']), int(self.position['y'])))

    def check_in_bounds(self, distance, direction=1):
        """ Check if the robot moving distance steps in direction is valid.
            
            If the robot would end up outside its safe area by moving,
            then return False to cancel the move.
            Otherwise return True.
        """

        x_diff = int(distance*math.sin(self.angle)*direction)
        y_diff = int(distance*math.cos(self.angle)*direction)

        potential_x = int(self.position['x'] + x_diff)
        potential_y = int(self.position['y'] + y_diff)

        if potential_x not in range(-100, 101):
            return False
        elif potential_y not in range(-200, 201):
            return False
        elif self.is_path_blocked(self.position['x'], self.position['y'], potential_x,  potential_y):
            self.obstacle_met = True
            return False
        return True

    def cant_fly_off_cliff(self):
        """ Print a reply stating the robot will not move past an obstacle/its safe zone. """
        if self.obstacle_met:
            print('{}: Sorry, There is an obstacle in the way.'.format(self.name))
            self.obstacle_met = False
        else:
            print('{}: Sorry, I cannot go outside my safe zone.'.format(self.name))