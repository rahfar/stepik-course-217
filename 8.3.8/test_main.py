import subprocess
import pathlib
from typing import ByteString


def run_module(input: ByteString, output: ByteString):
    res = subprocess.run(
        ["python", "main.py"],
        input=input,
        capture_output=True,
        cwd=pathlib.Path(__file__).parent,
    )
    assert output.decode("utf-8").strip() == res.stdout.decode("utf-8").strip()


def test_1():
    input = b"""ab
a
"""
    output = b"""1
"""
    run_module(input, output)

def test_2():
    input = b"""short
ports
"""
    output = b"""3
"""
    run_module(input, output)
