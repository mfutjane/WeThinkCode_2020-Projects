import math
import sys
from io import StringIO

# decide what to import by checking if the user asked for turtle or not
args = sys.argv[1:]
if len(args) == 1 and args[0] == 'turtle':
    from world.turtle import world
else:
    from world.text import world

def robot_start():
    """ Create a robot and turn it on. """

    new_robot = RobotMove()
    new_robot.loop()

class RobotMove(world.World):
    """ Create a new robot and allow it to move in a 2D space. """

    def __init__(self):
        """ Initialise world, set name, declare valid commands, and output obstacles. """

        world.World.__init__(self, 'Temp')

        self.name = self.new_name()
        self.draw_obs()
        self.set_name(self.name)

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

    def draw_obs(self):
        """ Draw obstacles in turtle or tell user where obstacles are in terminal. """

        if 'turtle' in sys.modules:
            for obs in self.my_obstacles:
                self.the_robot.begin_fill()
                self.the_robot.up()
                self.the_robot.goto(obs[0][0], obs[1][0])
                self.the_robot.goto(obs[0][0], obs[1][1])
                self.the_robot.goto(obs[0][1], obs[1][1])
                self.the_robot.goto(obs[0][1], obs[1][0])
                self.the_robot.goto(obs[0][0], obs[1][0])
                self.the_robot.end_fill()
            self.the_robot.home()
            self.the_robot.down()
        elif self.my_obstacles:
            print("There are some obstacles:")
            for obs in self.my_obstacles:
                print(f"- At position {obs[0][0]},{obs[1][0]} (to {obs[0][1]},{obs[1][1]})")

    def run_command(self, cmd):
        """ Run the given command. """

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
        """ Run all n movement commands. n should be in command. """

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
        """ Return a start and end position for replay command. """

        if args and args[0].isnumeric():
            return len(self.history)-int(args[0]), len(self.history)
        if args and self.digit_or_range(args[0]):
            range_list = args[0].split('-')
            return int(range_list[1])-1, int(range_list[0])-1
        return 0, len(self.history)

    def run(self, elem):
        """ If silent, run with output compressed. Otherwise, run normally. """

        if self.silent:
            sys.stdout, temp = StringIO(), sys.stdout
            self.run_command(elem)
            sys.stdout = temp
        else:
            self.run_command(elem)

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
        """ Return if command is a valid version of replay and its flags. """

        command = command[1:]
        command = [flag.lower() for flag in command]
        other = [flag for flag in command if self.digit_or_range(flag)]

        self.reversed = 'reversed' in command
        self.silent = 'silent' in command
        return len(command) == int(self.reversed) + int(self.silent) + len(other)

    def digit_or_range(self, string):
        """ Return if string is a digit or a range i.e '1' or '9-3'. """

        if string.isnumeric():
            return True
        string = string.split('-')
        if len(string) == 2 and string[0].isnumeric() and string[1].isnumeric():
            return True
        return False

if __name__ == '__main__':
    robot_start()