#!/usr/bin/env python
""" Test Driven Development Kata5: Point of sale kata.

Kata 5: Point of sale kata

Create a simple app for scanning bar codes to sell products.

Requirements

1. Barcode "12345" should display price "$7.25"

2. Barcode "23456" should display price "$12.50"

3. Barcode "99999" should display "Error: barcode not found"

4. Empty barcode should display "Error: empty barcode"

5. Introduce a concept of "total" command where it is possible to scan multiple items.
The command would display the sum of the scanned product prices

Reference: https://tddmanifesto.com/exercises/


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

################################################################################
# Imports

################################################################################
# Variables
barcode_dict = {12345:"7.25", 23456:"12.50", 45456:"5.25"}
total_price:float = 0.00
################################################################################
# Functions
def proc_barcode(barcode:int)->str:
    """processing barcode

    Args:
        barcode (int): barcode value

    Raises:
        TypeError: TypeError if barcode not int

    Returns:
        _type_: returns the price if barcode is known
    """
    global total_price

    if not isinstance(barcode, int):
        raise TypeError

    try:
        price = get_barcode(barcode)
        total_price += price
        return f"${price:.2f}"
    except ValueError as err:
        return err.args[0]

def get_barcode(barcode:int)->float:
    """_summary_

    Args:
        barcode (int): _description_

    Returns:
        float: _description_
    """
    if barcode not in barcode_dict:
        raise ValueError("Error: barcode not found")

    return float(barcode_dict[barcode])

def get_total()->str:
    """This function calculates the totals of all valid
        barcode prices handed over. After return the
        summary price varable is reset.

    Returns:
        str: accumulated price in $
    """
    global total_price

    totals = total_price
    total_price = 0.0
    return(f"${totals:.2f}")

################################################################################
# Classes
################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- any module script ---')
    val = proc_barcode(12345)
    print(val)
