import unittest
from unittest.mock import patch
from main import main
import io
import sys


class Test(unittest.TestCase):
    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = """4
""".split(
            "\n"
        )
        expected_output = """2
1 3
"""
        with patch("builtins.input", side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        user_input = """6
""".split(
            "\n"
        )
        expected_output = """3
1 2 3
"""
        with patch("builtins.input", side_effect=user_input):
            result = main()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
