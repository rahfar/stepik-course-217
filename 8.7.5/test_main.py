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
    input = b"""1
"""
    output = b"""0
1
"""
    run_module(input, output)

def test_2():
    input = b"""5
"""
    output = b"""3
1 3 4 5
"""
    run_module(input, output)

def test_3():
    input = b"""96234
"""
    output = b"""14
1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234
"""
    run_module(input, output)
