""" pytest module for caesar module.

This module defines the tests for the caesar.py module. Further explains of
pytest and unit tests can be found here in this video (german):
https://youtu.be/db2Iq2JHwiQ
https://docs.pytest.org/en/7.2.x/
https://docs.pytest.org/en/7.2.x/getting-started.html#get-started
https://docs.python.org/3/library/unittest.html


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
__contact__ = "github"
__copyright__ = "Copyright 2023, WShield"
__credits__ = ["Real Python"]
__date__ = "2023/09/04"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Development"
__version__ = "0.0.1"

################################################################################
# Imports

import pytest
from src.caesar import caesar_cipher

################################################################################
# Test Functions
@pytest.mark.parametrize("in1, in2, expected", [(1, "4", 0), ("a", "4", 0), (1, 3, 0), (None, 3, 0)])
def test_given_wrong_types_args_caesar_will_return_type_exep(in1, in2, expected):
    """test for valid input parameter types
    """

    with pytest.raises(TypeError):
        assert caesar_cipher(in1, in2)

def test_given_empty_string_caesar_will_return_empty_string():
    """Test Case to check that the input string of none returns a none
    """
    assert caesar_cipher("", 4) == ""

@pytest.mark.parametrize("in1, in2, expected", [("This is Text", 0, "This is Text"), ("another", 0, "another"), ("abcdefghijklmnopqrstuvwxyz", 0, "abcdefghijklmnopqrstuvwxyz")])
def test_given_zero_for_shifts_will_return_equal_text(in1, in2, expected):
    """Test Case to check that the teyt will be equal if 0 shifts is selected
    """

    assert expected == caesar_cipher(in1, in2)

def test_given_only_alpha_string_caeser_will_return_cipher(caesar_simple_test_data):
    """Test Case to check for simple alpha numerical strings and return them correct.
    """
    in1, in2, expected = caesar_simple_test_data
    assert expected == caesar_cipher(in1, in2)

def test_given_strings_with_mix_alpha_num_caeser_will_return_cipher(caesar_simple_mixed_test_data):
    """Test Case to check if only alphabetical values are coded.
    """
    in1, in2, expected = caesar_simple_mixed_test_data
    assert expected == caesar_cipher(in1, in2)

def test_given_rollover_strings_caeser_will_return_cipher(caesar_test_data):
    """Test Case to check the borders of alphabet
    """
    in1, in2, expected = caesar_test_data
    assert expected == caesar_cipher(in1, in2)

def test_given_a_long_text_including_spaces_caesar_converts_cipher(caesar_story_data):
    """Test Case for a longer string text out of curiosity"""
    in1, in2, expected = caesar_story_data
    assert expected == caesar_cipher(in1, in2)

def test_given_reverse_shift_caesar_converts_cipher(caesar_reverse_data):
    """Test Case to check for negative shift operations across edges"""
    in1, in2, expected = caesar_reverse_data
    assert expected == caesar_cipher(in1, in2)
