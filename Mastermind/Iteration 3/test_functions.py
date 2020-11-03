import sys
import unittest
import mastermind
from unittest.mock import patch
from contextlib import contextmanager
from io import StringIO

def in_range(code):
        for elem in code:
            if not elem in range(1, 9):
                return False
        return True

@contextmanager
def get_output(func, *args, **kwargs):
    #swap out sys io stream with ours for now, keep old output stream in out
    out, sys.stdout = sys.stdout, StringIO()
    try:
        func(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdout = out

@contextmanager
def sim_input(func, custom_stream, *args, **kwargs):
    #swap out sys io stream with ours for now, keep old output stream in out
    temp_in, temp_out, sys.stdout, sys.stdin = sys.stdin, sys.stdout, StringIO(), custom_stream
    try:
        func(*args, **kwargs)
        sys.stdout.seek(0)
        yield sys.stdout.read()
    finally:
        sys.stdin, sys.stdout = temp_in, temp_out


class MyTests(unittest.TestCase):

    def test_code(self):
        for i in range(100):
            code = mastermind.create_code()
            self.assertEqual(len(code), 4)
            self.assertTrue(in_range(code))

    def test_check_correctness(self):
        with get_output(mastermind.check_correctness, 4, 3) as output:
            self.assertEqual(output, 'Congratulations! You are a codebreaker!\n')
        
        with get_output(mastermind.check_correctness, 2, 4) as output:
            self.assertEqual(output, 'Turns left: 8\n')

        self.assertTrue(mastermind.check_correctness(4, 4))
        self.assertFalse(mastermind.check_correctness(2, 4))

    def test_get_guess(self):
        with sim_input(mastermind.get_guess, StringIO('5436\n')) as output:
            self.assertEqual('Input 4 digit code: ', output)

        with sim_input(mastermind.get_guess, StringIO('123456\n5678')) as output:
            self.assertEqual('Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ', output)

        with sim_input(mastermind.get_guess, StringIO('999\n5678')) as output:
            self.assertEqual('Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ', output)

        with sim_input(mastermind.get_guess, StringIO('abcd\n5678')) as output:
            self.assertEqual('Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ', output)


    @patch('sys.stdin', StringIO('5678\n'))
    def test_take_turn_correct(self):
        self.assertEqual((4, 0), mastermind.take_turn([5, 6, 7, 8]))

    @patch('sys.stdin', StringIO('5678\n'))
    def test_take_turn_incorrect(self):
        self.assertEqual((0, 0), mastermind.take_turn([1, 2, 3, 4]))

    @patch('sys.stdin', StringIO('5678\n'))
    def test_take_turn_semicorrect(self):
        self.assertEqual((2, 2), mastermind.take_turn([5, 6, 8, 7]))

    @patch('sys.stdin', StringIO('5678\n'))
    def test_take_turn_semicorrect_2(self):
        self.assertEqual((0, 4), mastermind.take_turn([8, 7, 6, 5]))