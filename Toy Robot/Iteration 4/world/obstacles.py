import itertools
import random

class Obstacles:

    def __init__(self):
        """ Define a set of obstacles and store them. """

        self.my_obstacles = []

        for _ in range(random.randint(1, 10)):
            x, y = random.randint(-100, 96), random.randint(-200, 196)
            while (x,y) in self.my_obstacles:
                x, y = random.randint(-100, 96), random.randint(-200, 196)
            self.my_obstacles.append(((x, x+4), (y, y+4)))
    
    def is_position_blocked(self, x, y):
        """ Return if position x,y is blocked. """

        for obs in self.my_obstacles:
            x_range = range(obs[0][0], obs[0][1]+1)
            y_range = range(obs[1][0], obs[1][1]+1)
            if x in x_range and y in y_range:
                return True
        return False

    def is_path_blocked(self, x1, y1, x2, y2):
        """ Return if path between x1,y1 and x2,y2 is blocked. """

        possible_pos = itertools.product(range(x1, x2+1), range(y1, y2+1))
        for possible_position in possible_pos:
            if self.is_position_blocked(possible_position[0], possible_position[1]):
                return True
        return False

    def get_obstacles(self):
        """ Return obstacles. """

        return self.my_obstacles