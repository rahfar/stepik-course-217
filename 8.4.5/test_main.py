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
    assert output.decode("utf-8").strip() == res.stdout.decode("utf-8").strip()


def test_1():
    input = b"""10 3
1 4 8
"""
    output = b"""9
"""
    run_module(input, output)
