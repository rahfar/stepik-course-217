import unittest
from unittest.mock import patch
from main import main
import io
import sys


class Test(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = """5 1 5 8 12 13
5 8 1 23 1 11
""".split(
            "\n"
        )
        expected_output = """3 1 -1 1 -1
"""
        with patch("builtins.input", side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
