#!/usr/bin/env python
""" Test Driven Development Kata4: seach citie names.

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
__date__ = "2022/11/19"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

def search_city(search_str:str):
    """Searches for the cities

    """
    cities = ["Paris" , "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", "Amsterdam", "Vienna", "Sydney", "New York City", "London", "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"]

    check_for_type_errors(search_str)

    if is_string_too_short(search_str):
        return None

    if is_string_complete_list_request(search_str):
        return print_cities(cities)

    result_cities = search(search_str, cities)
    return print_cities(result_cities)


def check_for_type_errors(val:str):
    """
        This function is checking all type errors
    """
    if not isinstance(val, str):
        raise TypeError
    if not val.isalpha() and not val == "*":
        raise TypeError

def is_string_complete_list_request(val:str):
    """
        This function will check if user request the
        complete list
    """
    return val is not None and val == "*"

def is_string_too_short(val:str):
    """
        This function is checking the search string length
    """
    return val is not None and len(val) < 2 and not is_string_complete_list_request(val)

def search(val:str, search_list):
    """
        This function is searching for val in list
    """
    result = []

    for elem in search_list:
        if elem.startswith(val) or -1 != elem.find(val):
            result.append(elem)
    return result

def print_cities(city_list):
    """
        This function converts the city list to a comma separated string
    """
    if city_list is not None and len(city_list) != 0:
        return ', '.join(city for city in city_list)
    return None




#if __name__ == "__main__":
#    print(search_city("*"))
