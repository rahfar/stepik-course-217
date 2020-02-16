import unittest
from unittest.mock import patch
from main import main
import io
import sys

class Test(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''1 1
a: 0
0
'''.split('\n')
        expected_output = '''a
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
'''.split('\n')
        expected_output = '''abacabad
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()