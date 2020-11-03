import unittest
import robot
import sys
from maze import obstacles
from unittest.mock import patch
from math import pi
from io import StringIO

class MyRobotTests(unittest.TestCase):

    @patch("sys.stdin", StringIO('Tancred\n1234\n   \nOkay'))
    def test_new_name(self):
        sys.stdout, temp = StringIO(), sys.stdout

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
        self.assertEqual(outputs[4], ' > Tancred moved forward by 10 steps.\n')
        self.assertEqual(outputs[6], 'Tancred: Shutting down..\n')

    @patch('sys.stdin', StringIO("Tancred\nforward 10\nback 3\noff\n"))
    def test_replay_n(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.loop()
        test_robot.replay(['replay', '1'])
        sys.stdout.seek(0)
        outputs = sys.stdout.readlines()

        self.assertTrue(' > Tancred replayed 1 commands.\n' in outputs)
        sys.stdout = temp

    @patch('sys.stdin', StringIO("Tancred\nforward 10\nback 3\noff\n"))
    def test_replay(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test
        sys.stdout = temp

        sys.stdout, temp = StringIO(), sys.stdout

        test_robot.loop()
        test_robot.replay(['replay'])
        sys.stdout.seek(0)
        outputs = sys.stdout.readlines()

        self.assertTrue(' > Tancred replayed 2 commands.\n' in outputs)
        sys.stdout = temp

    @patch('sys.stdin', StringIO("Tancred\nforward 10\nback 3\noff\n"))
    def test_replay_start_end(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # run commands to occupy history
        test_robot.loop()
        
        self.assertEqual(test_robot.replay_start_end(['1']), (1, 2))
        self.assertEqual(test_robot.replay_start_end(['2-1']), (0, 1))
        self.assertEqual(test_robot.replay_start_end('Booooooooored'), (0, 2))

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

    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_replay_valid(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test

        self.assertTrue(test_robot.replay_valid(['replay', '2-1', 'silent']))
        self.assertTrue(test_robot.replay_valid(['replay', '1', 'reversed']))
        self.assertTrue(test_robot.replay_valid(['replay']))
        self.assertTrue(test_robot.replay_valid(['replay', 'silent']))

        self.assertFalse(test_robot.replay_valid(['replay', '2a-1', 'silent']))
        self.assertFalse(test_robot.replay_valid(['replay', '1', 'silento']))
        sys.stdout = temp
    
    @patch('sys.stdin', StringIO('Chaos\n'))
    def test_digit_or_range(self):
        sys.stdout, temp = StringIO(), sys.stdout
        test_robot = robot.RobotMove() # set a new name but compress output to not affect the stream used in the test

        self.assertTrue(test_robot.digit_or_range("2"))
        self.assertTrue(test_robot.digit_or_range("9-9"))

        self.assertFalse(test_robot.digit_or_range("2a-1"))
        self.assertFalse(test_robot.digit_or_range("silent"))
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