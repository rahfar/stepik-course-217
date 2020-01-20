import unittest
from unittest.mock import patch
from main import main
import io
import sys

class TestSum(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''3
1 3
2 5
3 6
'''.split('\n')
        expected_output = '''1
3
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''4
4 7
1 3
2 5
5 6
'''.split('\n')
        expected_output = '''2
3 6
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()