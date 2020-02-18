import unittest
from unittest.mock import patch
from main import main
import io
import sys

class Test(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
'''.split('\n')
        expected_output = '''200
500
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''8
Insert 200
Insert 10
Insert 5
Insert 500
ExtractMax
ExtractMax
ExtractMax
ExtractMax
'''.split('\n')
        expected_output = '''500
200
10
5
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()