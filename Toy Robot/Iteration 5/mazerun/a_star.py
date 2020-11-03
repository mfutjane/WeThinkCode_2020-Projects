import turtle
from sys import argv
from mazerun import priority_queue

class A_Star(priority_queue.MyPriorityQueue):

    def __init__(self):
        priority_queue.MyPriorityQueue.__init__(self)

    def find_start(self, edge):
        if 'right' in edge:
            return (99,199)
        if 'bottom' in edge:
            return (-99,-199)
        return (-99,199)

    def add_start_nodes(self, open_spaces, edge, robot_position):
        if 'right' in edge or 'left' in edge:
            self.add_side(open_spaces, robot_position)
        elif 'bottom' in edge or 'top' in edge:
            self.add_top_bottom(open_spaces, robot_position)
        else:
            self.add_top_bottom(open_spaces, robot_position)

    def add_side(self, open_spaces, robot_position):
        for shift in range(401):
            shifted_start = (self.start[0], self.start[1]-shift)
            if shifted_start in open_spaces:
                self.add_node(shifted_start, 'start', robot_position)
    
    def add_top_bottom(self, open_spaces, robot_position):
        for shift in range(201):
            shifted_start = (self.start[0]+shift, self.start[1])
            if shifted_start in open_spaces:
                self.add_node(shifted_start, 'start', robot_position)

    def find_path(self, open_spaces, edge, robot_position):
        self.start = self.find_start(edge)
        self.add_start_nodes(open_spaces, edge, robot_position)
        
        returned = ''
        while returned != str(robot_position):
            returned, pos = self.pop(open_spaces)
            # robot.goto(pos)
            # robot.dot(1)
        return returned