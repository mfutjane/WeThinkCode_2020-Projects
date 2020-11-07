import math
import sys
from io import StringIO

def robot_start():
    """ Create a robot and turn it on. """

    new_robot = RobotMove()
    new_robot.loop()

class RobotMove():
    """ Create a new robot and allows it to move in a 2D space. """

    def __init__(self):
        """ Set position, angle, name, and valid commands for the new robot. """

        self.position = {'x':0, 'y':0}
        self.angle = 0
        self.name = self.new_name()

        self.valid_cmds = {'forward': self.move_forward, 'back': self.move_back,
        'left': self.turn_left, 'right': self.turn_right, 'help':self.print_help,
        'sprint':self.sprint, 'off': self.off}

    def loop(self):
        """ Get a command as long as the robot is on. """

        on = True
        while on:
            cmd = self.get_command()
            while not self.is_cmd_valid(cmd):
                cmd = self.get_command()
            
            on = self.run_command(cmd)

    def run_command(self, cmd):
        if len(cmd) == 2:
            self.valid_cmds[cmd[0].lower()](int(cmd[1]))
        else:
            self.valid_cmds[cmd[0].lower()]()
        return cmd[0].lower() != 'off'

    def new_name(self):
        """ Prompt the user for a name and store as robot's name. """

        name = input('What do you want to name your robot? ')
        while len(name.strip()) == 0:
            print("Please name your robot.")
            name = input('What do you want to name your robot? ')
        print('{}: Hello kiddo!'.format(name))
        return name

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
        return True

    def off(self, *args):
        """ Return false to shut down the robot. """

        print('{}: Shutting down..'.format(self.name))
        return False

    def print_help(self, *args):
        """ Print information on valid commands. """
    
        print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD X - Move the robot X steps forward.
BACK X - Move the robot X steps backward.
LEFT - Turn the robot 90 degrees left.
RIGHT - Turn the robot 90 degrees right.
SPRINT X - Move the robot forward X steps, decrease X and move forward X steps again until X=0.""")

    def get_command(self):
        """ Prompt the user for a command and return it as a list. """

        cmd = input('{}: What must I do next? '.format(self.name))
        cmd = cmd.split()
        return cmd

    def is_cmd_valid(self, cmd):
        """ Return false if cmd is not handled by the robot, true otherwise. """

        if len(cmd) not in [1, 2] or cmd[0].lower() not in self.valid_cmds:
            cmd_str = " ".join(cmd)
            print("{}: Sorry, I did not understand '{}'.".format(self.name, cmd_str))
            return False
        return True

    def cant_fly_off_cliff(self):
        """ Print a reply stating the robot will not move past its safe zone. """

        print('{}: Sorry, I cannot go outside my safe zone.'.format(self.name))

if __name__ == '__main__':
    robot_start()
