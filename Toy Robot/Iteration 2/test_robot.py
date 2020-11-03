import unittest
import robot
import sys
from unittest.mock import patch
from math import pi
from io import StringIO

class MyRobotTests(unittest.TestCase):

    @patch("sys.stdin", StringIO('Tancred\n1234\n   \nOkay'))
    def test_new_name(self):
        sys.stdout, temp = StringIO(), sys.stdout
        #test_robot = robot.RobotMove()

        self.assertEqual(robot.RobotMove.new_name(self), "Tancred")
        self.assertEqual(robot.RobotMove.new_name(self), "1234")
        self.assertEqual(robot.RobotMove.new_name(self), "Okay")
        
        sys.stdout.seek(0)
        outputs = sys.stdout.readlines()
        sys.stdout = temp
        
        self.assertEqual(outputs[0], 'What do you want to name your robot? Tancred: Hello kiddo!\n')
        self.assertEqual(outputs[2], 'What do you want to name your robot? Please name your robot.\n')
        self.assertEqual(outputs[3], 'What do you want to name your robot? Okay: Hello kiddo!\n')
    
    @patch('sys.stdin', StringIO("Tancred\n"))
    def test_run_command(self):
        sys.stdout, temp = StringIO(), sys.stdout
        
        test_robot = robot.RobotMove()
        fwd_res = test_robot.run_command(['forward', '10'])
        off_res = test_robot.run_command(["Off"])

        sys.stdout.seek(0)
        outputs = sys.stdout.readlines()
        sys.stdout = temp

        self.assertTrue(fwd_res)
        self.assertFalse(off_res)
        self.assertEqual(outputs[1], ' > Tancred moved forward by 10 steps.\n')
        self.assertEqual(outputs[3], 'Tancred: Shutting down..\n')

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_turn_right(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.turn_right()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos turned right.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos now at position (0,0).\n')
        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_turn_left(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.turn_left()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), ' > Chaos turned left.\n')
        self.assertEqual(sys.stdout.readline(), ' > Chaos now at position (0,0).\n')
        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_move_forward(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

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
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

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
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
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
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        self.assertFalse(test_robot.check_in_bounds(1000))
        self.assertTrue(test_robot.check_in_bounds(23))
        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_update_position(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
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
    
    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_is_cmd_valid(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        self.assertTrue(test_robot.is_cmd_valid(['off']))
        self.assertFalse(test_robot.is_cmd_valid(['offISH']))
        
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.readline(), "Chaos: Sorry, I did not understand 'offISH'.\n")

        sys.stdout = temp

    @patch('sys.stdin', StringIO('Chaos\nforward 10\noff\n'))
    def test_get_command(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        self.assertEqual(test_robot.get_command(), ['forward', '10'])
        
        sys.stdout.seek(0)

        self.assertEqual(sys.stdout.readline(), 'Chaos: What must I do next? ')

        sys.stdout = temp

if __name__ == '__main__':
    unittest.main()