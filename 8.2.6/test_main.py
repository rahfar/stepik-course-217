import subprocess
import pathlib
from typing import ByteString


def run_module(input: ByteString, output: ByteString):
    res = subprocess.run(
        ["python", "main.py"],
        input=input,
        capture_output=True,
        cwd=pathlib.Path(__file__).parent,
        check=True,
    )
    assert output == res.stdout


def test_1():
    input = b"""5
5 3 4 4 2
"""
    output = b"""4
1 3 4 5
"""
    run_module(input, output)
