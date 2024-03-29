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
    input = b"""4
3 6 7 12
"""
    output = b"""3
"""
    run_module(input, output)
