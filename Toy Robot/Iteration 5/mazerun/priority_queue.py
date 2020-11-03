import math

class Node:

    def __init__(self, position, fastest_node_here, blocked_rating, robot_position):
        self.name = str(position)
        self.position = position
        self.robot_position = robot_position
        self.distance = math.sqrt((position[0] - robot_position[0])**2+(position[1] - robot_position[1])**2)
        self.overall = self.distance + blocked_rating*0
        self.fastest_node_here = fastest_node_here

class MyPriorityQueue:

    def __init__(self):
        self.queue = []
        self.graveyard = []
        self.node_dicts = dict()

    def add_node(self, position, fastest_node_here, robot_position):
        new_node = Node(position, fastest_node_here, 0, robot_position)
        
        for item in self.graveyard:
            if item.name == new_node.name:
                return 

        for item in self.queue:
            if new_node.overall <= item.overall:
                index_to_replace = self.queue.index(item)
                self.queue.insert(index_to_replace, new_node)
                self.graveyard.append(new_node)
                break
            elif self.queue.index(item) == len(self.queue)-1:
                self.queue.append(new_node)
                self.graveyard.append(new_node)
                break

        if not self.queue:
            self.queue.append(new_node)

    def pop(self, open_spaces):
        top_node = ''
        try:
            top_node = self.queue[0]
        except IndexError: 
            print('blocked')
            return 'Blocked', (0,0)

        self.queue = self.queue[1:]

        self.node_dicts[top_node.name] = top_node
        self.graveyard.append(top_node)

        left = (top_node.position[0]-1, top_node.position[1])
        right = (top_node.position[0]+1, top_node.position[1])
        up = (top_node.position[0], top_node.position[1]+1)
        down = (top_node.position[0], top_node.position[1]-1)
        # tr = (top_node.position[0]+1, top_node.position[1]+1)
        # br = (top_node.position[0]+1, top_node.position[1]-1)
        # tl = (top_node.position[0]-1, top_node.position[1]+1)
        # bl = (top_node.position[0]-1, top_node.position[1]-1)

        for node in [left, right, down, up]:
            if node[0] in range(-100, 100) and node[1] in range(-200, 201) and (node[0], node[1]) in self.open_spaces:
                self.add_node(node, top_node.name, top_node.robot_position)
        return top_node.name, top_node.position

    def postion_blocked(self, x, y, obstacles_):
        """ Return if position x,y is blocked. """

        for obs in obstacles_:
            x_range = range(obs[0][0], obs[0][1]+1)
            y_range = range(obs[1][0], obs[1][1]+1)
            if x in x_range and y in y_range:
                return True
        return False