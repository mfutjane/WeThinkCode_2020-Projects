import unittest
import world.text.world as robot
import sys
import world.text.world as obstacles
from unittest.mock import patch
from math import pi
from io import StringIO

class MyRobotTests(unittest.TestCase, robot.World):

    def create_robot_silently(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.World('Chaos') # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp
        return test_robot

    def test_turn_right(self):
        test_robot = self.create_robot_silently()
        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.turn_right()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos turned right.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos now at position (0,0).\n')
        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_turn_left(self):
        test_robot = self.create_robot_silently()
        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.turn_left()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos turned left.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos now at position (0,0).\n')
        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_move_forward(self):
        test_robot = self.create_robot_silently()
        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.move_forward(10)
        test_robot.move_forward(233)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved forward by 10 steps.\n')
        sys.stdout.readline()
        self.assertEqual(sys.stdout.readline(), 'Chaos: Sorry, I cannot go outside my safe zone.\n')

        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_move_back(self):
        test_robot = self.create_robot_silently()
        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.move_back(10)
        test_robot.move_back(233)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved back by 10 steps.\n')
        sys.stdout.readline()
        self.assertEqual(sys.stdout.readline(), 'Chaos: Sorry, I cannot go outside my safe zone.\n')

        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_sprint(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.World('Chaos') # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.sprint(5)
        test_robot.sprint(55)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved forward by 5 steps.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved forward by 4 steps.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved forward by 3 steps.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved forward by 2 steps.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos moved forward by 1 steps.\n')
        sys.stdout.readline()
        self.assertEqual(sys.stdout.readline(), 'Chaos: Sorry, I cannot go outside my safe zone.\n')

        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_check_in_bounds(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.World('Chaos') # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        self.assertFalse(test_robot.check_in_bounds(1000))
        self.assertTrue(test_robot.check_in_bounds(23))
        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_update_position(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.World('Chaos') # set a new name but compress output to not affect the stream used in the test
        test_robot.move_back(10) # move robot around
        test_robot.turn_left()
        test_robot.move_forward(3)
        test_robot.turn_right()
        test_robot.move_forward(7)        
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.update_position()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos now at position (-3,-3).\n')
        sys.stdout.readline()

        sys.stdout = temp

if __name__ == "__main__":
    unittest.main()
    