from .compiler import *
import pytest


def test_acc_plus():
    code = """acc +3"""
    assert Compiler.run(code) == 3

def test_acc_minus():
    code = """acc -3"""
    assert Compiler.run(code) == -3

def test_multi_acc():
    code = """acc -3
    acc +5
    acc -3
    acc 0"""
    assert Compiler.run(code) == -1

def test_jmp_ahead():
    code = "jmp +10"
    assert Compiler(code).execute_line(0) == 10

def test_unknown_instruction():
    code = """bleh +3"""
    with pytest.raises(UnknownInstructionError):
        Compiler.run(code)

def test_parse_error():
    code = """no.space"""
    with pytest.raises(ParseError):
        Compiler.run(code)

def test_day8_pt1():
    
    code = """nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6"""
    with pytest.raises(RepeatedLineError):
        Compiler(code).execute(raise_on_repeat=True)
