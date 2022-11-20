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
from src.string_calc import calculate_int_from_string

def test_given_an_empty_string_calc_int_from_string_will_return_zero():
    """
        Test the calculate string function on empty string return.
    """
    val = calculate_int_from_string("")
    assert val == 0

def test_given_a_one_calc_int_from_string_will_return_zero():
    """
        This function will test if paramter = 0 will return 0
    """
    val = calculate_int_from_string("0")
    assert val == 0

def test_given_a_one_calc_int_from_string_will_return_one():
    """
        This function will test if paramter = 1 will return 0
    """
    val = calculate_int_from_string("1")
    assert val == 1

def test_given_a_not_valid_string_calc_int_from_string_will_throw_exeption():
    """
        This function will test if a non valid string results in an exception
    """
    with pytest.raises(ValueError):
        assert calculate_int_from_string("1.011")
    
    with pytest.raises(ValueError):
        assert calculate_int_from_string("1.0")

def test_given_less_than_two_numbers_calculate_int_from_string_will_throw_exception():
    """
        This function will test that not more than two numbers are passed.
    """
    with pytest.raises(ValueError):
        assert calculate_int_from_string("1,2,3")
    