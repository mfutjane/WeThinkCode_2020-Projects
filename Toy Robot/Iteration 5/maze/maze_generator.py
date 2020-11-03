import random

__name__ == "Maze Generator"

class Obstacles:

    def __init__(self):
        """ Define a set of obstacles and store them. """

        self.my_obstacles = []
        self.previous_row_equations = []
        self.possible_dimensions = [1, 2, 4, 5, 8, 10, 20]
        self.possible_dimensions.append(5)
        self.create_obstacles()

    def create_obstacles(self):
        """
        Break up the area into dimension*dimension blocks.
        For every block, shift the start point and create 
        obstacles in each block according to its local
        x and y.
        """

        dimension = random.choice(self.possible_dimensions)
        # dimension = 4 uncomment if you want to test certain values
        y_shift = int(400/dimension)
        x_shift = int(200/dimension)

        equations = [self.vertical, self.horizontal]
        for y in range(dimension):
            lines = [random.choice(equations) for _ in range(dimension-2)]
            lines.append(self.vertical)
            lines.append(self.horizontal)
            lines = self.ensure_exits(lines)
            for x in range(dimension):
                starting_point = -100 + x_shift*x, 200 - y_shift*y
                self.generate_obstacles(dimension, starting_point, y_shift, x_shift, lines.pop(0))

    def ensure_exits(self, lines):

        if len(self.previous_row_equations) == 0:
            for i in lines:
                self.previous_row_equations.append(i)
            return lines

        for i in range(len(lines)):
            if lines[i](0, 1) == self.previous_row_equations[i](0, 1) and  lines[i](0, 1) == True: # they are vert
                lines[i] = self.horizontal
            elif lines[i](0, 1) == self.previous_row_equations[i](0, 1) and lines[i](0, 1) == False: # they are horiz
                lines[i] = self.vertical

        self.previous_row_equations = []
        for i in lines:
            self.previous_row_equations.append(i)
        return lines

    def generate_obstacles(self, dimension, starting_point, y_shift, x_shift, line):
        """
        Pick an equation for each block. Go through each point 
        and decide if it should be an obstacle using the picked equation.
        """

        for y in range(y_shift+1):
            for x in range(x_shift+1):
                current_point = starting_point[0]+x, starting_point[1]-y
                central_point = starting_point[0]+int(x_shift/2), starting_point[1]-int(y_shift/2)
                self.on_the_line(current_point, dimension, central_point, line)

    def on_the_line(self, point, dimension, start, equation):
        """
        Localise the given point and decide if it is on the line
        of the equation.
        """
        
        relative_x = point[0] - start[0] # start - dimension makes it relative to the center of the block
        relative_y = point[1] - start[1]
        point_is_legal = point[0] in range(-98, 98) and point[1] in range(-198, 198)
        point_not_blocking_player = not (point[0] in range(-10, 11) and point[1] in range(-10, 11))

        if equation(relative_x, relative_y) and point_is_legal and point_not_blocking_player:
            self.my_obstacles.append((point[0]-2, point[1]-2))

    def vertical(self, x, y):
        return x == 0

    def horizontal(self, x, y):
        return y == 0

    def is_position_blocked(self, x, y):
        """ Return if position x,y is blocked. """

        for obs in self.my_obstacles:
            x_range = range(obs[0], obs[0]+5)
            y_range = range(obs[1], obs[1]+5)
            if x in x_range and y in y_range:
                return True
        return False

    def is_path_blocked(self, x1, y1, x2, y2):
        """ Return if path between x1,y1 and x2,y2 is blocked. """

        for obs in self.my_obstacles:
            first_condition_x = x1 <= obs[0] and x2 >= obs[0] and x2 >= x1
            second_condition_x = x1 >= obs[0] and x2 <= obs[0] and x2 <= x1
            x_condition = first_condition_x or second_condition_x

            first_condition_y = y1 <= obs[1] and y2 >= obs[1] and y2 >= y1
            second_condition_y = y1 >= obs[1] and y2 <= obs[1] and y2 <= y1
            y_condition = first_condition_y or second_condition_y

            if x_condition and y_condition:
                return True
        return False

    def get_inner_obstacles(self):
        """ Return obstacles. """

        return self.my_obstacles

def get_obstacles():
    new_maze = Obstacles()
    return new_maze.get_inner_obstacles()