#!/usr/bin/env python
""" Test Driven Development Test: string calculator.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Stephan Wink"
__copyright__ = "Copyright $2022, $WShield"
__credits__ = ["MArtin C. Roberts"]
__date__ = "2022/11/20"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

import pytest
from src.fizzbuzz import calculate_fizzbuzz

def test_given_input_number_is_zero_calculating_fizzbuzz_will_return_zero():
    """
        This function tests that calc FizzBuzz returns zero if given
        input number is zero.  
    """
    val = calculate_fizzbuzz(0)
    assert val == "0"

def test_given_input_as_float_calculating_fizzbuzz_will_return_with_exception():
    """
        This test checks that for a given input as float will generate
        an exception.
    """
    with pytest.raises(ValueError):
        assert calculate_fizzbuzz(3.141)

def test_given_input_as_string_calculating_fizzbuzz_will_return_with_exception():
    """
        This function tests that for a given input string will generate an exception.
    """
    with pytest.raises(ValueError):
        assert calculate_fizzbuzz("one")

def test_given_input_is_one_calculating_fizzbuzz_will_return_with_one():
    """
        This function will check that the given string 1 is returning 1.
    """
    val = calculate_fizzbuzz(1)
    assert val == "1"

def test_given_input_is_three_calculating_fizzbuzz_will_return_fizz():
    """
        This function checks that a given int 3 will generate the string "Fizz".
    """
    val = calculate_fizzbuzz(3)
    assert val == "Fizz"

def test_given_input_is_five_calculating_fizzbuzz_will_return_buzz():
    """
        This function checks that a given 5 will generate the string "Buzz".
    """
    val = calculate_fizzbuzz(5)
    assert val == "Buzz"

def test_given_input_is_multi_o_three_and_five_calculating_fizzbuzz_will_return_fizzbuzz():
    """
        This function checks that a multiple of 3 or 5 will return "FizzBuzz".
    """
    val = calculate_fizzbuzz(15)
    assert val == "FizzBuzz"
    val = calculate_fizzbuzz(30)
    assert val == "FizzBuzz"
    val = calculate_fizzbuzz(120)
    assert val == "FizzBuzz"