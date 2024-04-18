import pytest
import allure

def pow_2(a):
    return a**2

def test_pow_2():
    assert pow_2(3) == 9

def test_pow_2_1():
    assert pow_2(4) == 16

def test_pow_2_2():
    assert pow_2(12) == 144

def test_pow_2_3():
    assert pow_2(24) == 5452