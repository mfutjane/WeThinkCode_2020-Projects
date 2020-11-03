import unittest
import random as myrand
from world import obstacles

class ObstaclesTest(unittest.TestCase):

    def test_obstacles_in_range(self):
        test_obstacle = obstacles.Obstacles()

        for obstacle in test_obstacle.get_obstacles():
            self.assertTrue(obstacle[0][0] in range(-100, 101)) # lower x
            self.assertTrue(obstacle[0][1] in range(-100, 101)) # larger x
            self.assertTrue(obstacle[1][0] in range(-200, 201)) # lower y
            self.assertTrue(obstacle[1][1] in range(-200, 201)) # larger y
    
    def test_is_position_blocked(self):
        obstacles.random.randint = lambda x, y: 1
        test_obstacle = obstacles.Obstacles()
        self.assertTrue(test_obstacle.is_position_blocked(2, 4))
        self.assertFalse(test_obstacle.is_position_blocked(15, 15))

    def test_is_path_blocked(self):
        obstacles.random.randint = lambda x, y: 1
        test_obstacle = obstacles.Obstacles()
        self.assertTrue(test_obstacle.is_path_blocked(0,0,10,10))
        self.assertFalse(test_obstacle.is_path_blocked(0,0,-10,-10))

if __name__ == "__main__":
    unittest.main()