import subprocess
from typing import ByteString


def run_module(input: ByteString, output: ByteString):
    res = subprocess.run(['python', 'main.py'],
                         input=input,
                         capture_output=True)
    assert output == res.stdout


def test_1():
    input = b'''2 3
0 5
7 10
1 6 11
'''
    output = b'''1 0 0
'''
    run_module(input, output)
