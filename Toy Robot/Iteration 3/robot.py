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

        self.reversed = False
        self.silent = False

        self.valid_cmds = {'forward': self.move_forward, 'back': self.move_back,
        'left': self.turn_left, 'right': self.turn_right, 'help':self.print_help,
        'sprint':self.sprint, 'off': self.off, 'replay': self.replay}
        self.history = []

    def loop(self):
        """ Get a command as long as the robot is on. """

        on = True
        while on:
            cmd = self.get_command()
            while not self.is_cmd_valid(cmd):
                cmd = self.get_command()
            
            if cmd[0].lower() not in ['replay', 'help', 'off']:
                self.history.append(cmd)
            on = self.run_command(cmd)

    def run_command(self, cmd):
        if cmd[0].lower() == 'replay':
            self.replay(cmd)
        elif len(cmd) == 2:
            self.valid_cmds[cmd[0].lower()](int(cmd[1]))
        else:
            self.valid_cmds[cmd[0].lower()]()
        return cmd[0].lower() != 'off'

    def new_name(self):
        """ Prompt the user for a name and store as robot's name. """

        name = input('What do you want to name your robot? ')
        while len(name.strip()) == 0:
            print('Please name your robot.')
            name = input('What do you want to name your robot? ')
        print('{}: Hello kiddo!'.format(name))
        return name

    def replay(self, command):
        num = [num for num in command if self.digit_or_range(num)]
        start, end = self.replay_start_end(num)

        temp_history = self.history[::-1] if self.reversed else self.history
        temp_history = temp_history[start: end]
        
        for elem in temp_history:
                self.run(elem)

        output = " > {} replayed {} commands".format(self.name, len(temp_history))
        output = output + ' in reverse' if self.reversed else output
        output = output + ' silently' if self.silent else output
        
        print(output + '.')
        self.update_position()

    def replay_start_end(self, args):
        if args and args[0].isnumeric():
            return len(self.history)-int(args[0]), len(self.history)
        if args and self.digit_or_range(args[0]):
            range_list = args[0].split('-')
            return int(range_list[1])-1, int(range_list[0])-1
        return 0, len(self.history)

    def run(self, elem):
        if self.silent:
            sys.stdout, temp = StringIO(), sys.stdout
            self.run_command(elem)
            sys.stdout = temp
        else:
            self.run_command(elem)

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
HELP - provide information about commands""")

    def get_command(self):
        """ Prompt the user for a command and return it as a list. """

        cmd = input('{}: What must I do next? '.format(self.name))
        cmd = cmd.split()
        return cmd

    def is_cmd_valid(self, cmd):
        """ Return false if cmd is not handled by the robot, true otherwise. """

        if cmd[0].lower() == 'replay':
            if not self.replay_valid(cmd):
                cmd_str = " ".join(cmd)
                print("{}: Sorry, I did not understand '{}'.".format(self.name, cmd_str))
                return False
            return True

        if len(cmd) not in [1, 2] or cmd[0].lower() not in self.valid_cmds:
            cmd_str = " ".join(cmd)
            print("{}: Sorry, I did not understand '{}'.".format(self.name, cmd_str))
            return False
        return True

    def replay_valid(self, command):
        command = command[1:]
        command = [flag.lower() for flag in command]
        other = [flag for flag in command if self.digit_or_range(flag)]

        self.reversed = 'reversed' in command
        self.silent = 'silent' in command
        return len(command) == int(self.reversed) + int(self.silent) + len(other)

    def digit_or_range(self, string):
        if string.isnumeric():
            return True
            
        str_spl = string.split('-')
        if len(str_spl) == 2 and str_spl[0].isnumeric() and str_spl[1].isnumeric():
            return True
        return False

    def cant_fly_off_cliff(self):
        """ Print a reply stating the robot will not move past its safe zone. """

        print('{}: Sorry, I cannot go outside my safe zone.'.format(self.name))

if __name__ == '__main__':
    robot_start()