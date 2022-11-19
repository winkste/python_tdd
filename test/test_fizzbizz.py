import pytest
from src.fizzbizz import calculate_fizzbuzz

def test_givenInputNumberIsZero_calculatingFizzBizz_willReturnZero():
    val = calculate_fizzbuzz(0)
    assert val == "0"

def test_givenInputAsFloat_calculatingFizzBizz_willReturnWithException():
    with pytest.raises(ValueError):
        assert calculate_fizzbuzz(3.141)

def test_givenInputAsString_calculatingFizzBizz_willReturnWithException():
    with pytest.raises(ValueError):
        assert calculate_fizzbuzz("one")

def test_givenInputIsOne_calculatingFizzBizz_willReturnWithOne():
    val = calculate_fizzbuzz(1)
    assert val == "1"

def test_givenInputIsThree_calculatingFizzBizz_willReturnFizz():
    val = calculate_fizzbuzz(3)
    assert val == "Fizz"

def test_givenInputIsFive_calculatingFizzBuzz_willReturnBuzz():
    val = calculate_fizzbuzz(5)
    assert val == "Buzz"

def test_givenInputIsMultiOfThreeAndFive_calculatingFizzBuzz_willReturnFizzBuzz():
    val = calculate_fizzbuzz(15)
    assert val == "FizzBuzz"