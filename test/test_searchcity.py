#!/usr/bin/env python
""" Test Driven Development Test: KATA4 search city names

Kata 4 – Search functionality

Implement a city search functionality. The function takes a string (search text)
as input and returns the found cities which corresponds to the search text.

Prerequisites

Create a collection of strings that will act as a database for the city names.

City names: Paris, Budapest, Skopje, Rotterdam, Valencia, Vancouver, Amsterdam,
Vienna, Sydney, New York City, London, Bangkok, Hong Kong, Dubai, Rome, Istanbul

Requirements
1. If the search text is fewer than 2 characters, then should return no results.
(It is an optimization feature of the search functionality.)

2. If the search text is equal to or more than 2 characters, then it should return
all the city names starting with the exact search text.

For example for search text “Va”, the function should return Valencia and Vancouver
3. The search functionality should be case insensitive

4. The search functionality should work also when the search text is just a part of a
city name

For example “ape” should return “Budapest” city
5. If the search text is a “*” (asterisk), then it should return all the city names.

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
__date__ = "2022/11/30"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

import pytest
from src.searchcity import search_city


def test_given_not_string_search_cities_will_raise_exception():
    """
        This function will test for value exeptions
    """

    with pytest.raises(TypeError):
        assert search_city(123) is None
        assert search_city(["this is a string"]) is None
        assert search_city("") is None

def test_given_a_too_short_string_search_cities_will_return_none():
    """
        This function checks the minimum string size limit
    """
    assert search_city("v") is None

def test_given_is_not_alpha_search_cities_will_raise_type_error():
    """
        This function will test that a string is a word
    """
    with pytest.raises(TypeError):
        assert search_city("Vancouver123") is None

def test_given_vancouver_search_cities_will_return_vancouver():
    """
        This function will check if the city Vancouver is in the cities list
    """
    assert search_city("Vancouver") == "Vancouver"


def test_given_a_city_not_in_list_search_cities_will_return_none():
    """
        This function will test for a None if a city or word is not in list
    """

    assert search_city("Celle") is None

def test_given_a_lower_case_string_search_cities_will_return_none():
    """
        This function will test for lower case sensititvity
    """

    assert search_city("vancouver") is None

def test_given_asterix_search_city_will_return_all_cities():
    """
        This function will test all cities by using asterix "*"
    """

    assert search_city("*") == "Paris, Budapest, Skopje, Rotterdam, Valencia, Vancouver, Amsterdam, Vienna, Sydney, New York City, London, Bangkok, Hong Kong, Dubai, Rome, Istanbul"

def test_given_a_start_of_a_city_search_cities_will_return_the_city():
    """
        This function will test for a match when given a start of a city
    """

    assert search_city("Par") == "Paris"

def test_given_va_search_cities_will_return_two_cities_starting_with_va():
    """
        This function will test for more result fits in the list
    """

    assert search_city("Va") == "Valencia, Vancouver"

def test_given_ape_search_cities_will_return_budapest():
    """
        This function will test if the search operation also works with an
        inner sub string of the city like "ape" in Bud"ape"pest
    """

    assert search_city("ape") == "Budapest"
    assert search_city("dam") == "Rotterdam, Amsterdam"
