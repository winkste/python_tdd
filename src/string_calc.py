#!/usr/bin/env python
""" Test Driven Development Kata: string calculator.

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

def calculate_int_from_string(str_arg):
    """
        This function calculates an integer from one or more string values:
        So the inputs can be: “”, “1”, “1,2”. For an empty string, it will return 0.
    """
    if str_arg == "":
        return 0
    str_list = str_arg.split(",")
    if len(str_list) > 2:
        raise ValueError
    val = 0
    for i in str_list:
        val = val + int(i)
    return val
