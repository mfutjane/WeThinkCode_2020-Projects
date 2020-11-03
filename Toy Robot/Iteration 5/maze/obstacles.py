import itertools
import random

__name__ = 'obstacles'

class Obstacles:

    def __init__(self):
        """ Define a set of obstacles and store them. """

        self.my_obstacles = []
        for _ in range(random.randint(1, 10)):
            x, y = random.randint(-100, 96), random.randint(-200, 196)
            while (x,y) in self.my_obstacles:
                x, y = random.randint(-100, 96), random.randint(-200, 196)
            self.my_obstacles.append((x, y))
    
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
            x_match = (x1 >= obs[0] and x2 <= obs[0] and x2 < x1) or (x1 <= obs[0] and x2 >= obs[0] and x2 > x1)
            y_match = (y1 >= obs[1] and y2 <= obs[1] and x2 < x1) or (y1 <= obs[1] and y2 >= obs[1] and y2 > y1)
            if x_match and y_match:
                return True
        return False

    def get_obstacles(self):
        """ Return obstacles. """

        return self.my_obstacles