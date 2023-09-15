#!/usr/bin/env python
""" Pytest configuration file

Longer description of this module.

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
__date__ = "2023/09/06"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Development"
__version__ = "0.0.1"


################################################################################
# Imports
import pytest

################################################################################
# Variables

################################################################################
# Classes

################################################################################
# Functions

################################################################################
# Scripts

@pytest.fixture(params=[("ABC", 4, "EFG"), ("abc", 4, "efg")])
def caesar_simple_test_data(request):
    """Returns a tuple containing two input values and an expected \
    output value for the caesar_cipher method."""
    return request.param

@pytest.fixture(params=[("ABC.123", 4, "EFG.123"), ("abc!§$", 4, "efg!§$")])
def caesar_simple_mixed_test_data(request):
    """Returns a tuple containing two input values and an expected \
    output value for the caesar_cipher method."""
    return request.param

@pytest.fixture(params=[("ABC", 4, "EFG"), ("XYZ", 4, "BCD"), ("abc", 4, "efg"), ("xyz", 4, "bcd")])
def caesar_test_data(request):
    """Returns a tuple containing two input values and an expected \
    output value for the caesar_cipher method."""
    return request.param

@pytest.fixture(params=[("This is a novel and it starts from the beginning. It ends at the end!", 4, "Xlmw mw e rszip erh mx wxevxw jvsq xli fikmrrmrk. Mx irhw ex xli irh!")])
def caesar_story_data(request):
    """Returns a tuple containing two input values and an expected \
    output value for the caesar_cipher method."""
    return request.param

@pytest.fixture(params=[("EFG", -4, "ABC"), ("CDE", -4, "YZA"), ("efg", -4, "abc"), ("cde", -4, "yza")])
def caesar_reverse_data(request):
    """Returns a tuple containing two input values and an expected \
    output value for the caesar_cipher method."""
    return request.param