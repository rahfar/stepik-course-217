import unittest
from unittest.mock import patch
from main import main
import io
import sys

class Test(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = '''3 50
60 20
100 50
120 30
'''.split('\n')
        expected_output = '''180.000
'''
        with patch('builtins.input', side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()