import unittest
from unittest.mock import patch
from main import main
import io
import sys

class TestSum(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''18 35
'''.split('\n')
        expected_output = '''1
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)
    
    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''14159572 63967072
'''.split('\n')
        expected_output = '''4
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()