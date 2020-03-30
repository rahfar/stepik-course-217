import unittest
from unittest.mock import patch
from main import main
import io
import sys


class Test(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''5
2 3 9 2 9
'''.split('\n')
        expected_output = '''2
'''
        with patch('builtins.input', side_effect=user_input):
            main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''8
8 7 6 5 4 3 2 1
'''.split('\n')
        expected_output = '''28
'''
        with patch('builtins.input', side_effect=user_input):
            main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''8
1 2 3 4 5 6 7 8
'''.split('\n')
        expected_output = '''0
'''
        with patch('builtins.input', side_effect=user_input):
            main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_4(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''1
1
'''.split('\n')
        expected_output = '''0
'''
        with patch('builtins.input', side_effect=user_input):
            main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
