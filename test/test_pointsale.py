#!/usr/bin/env python
""" Test Driven Development Test: pointsale.

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
from src.pointsale import proc_barcode, get_total
#import conftest

@pytest.mark.parametrize("test_input,expected", [("Not Int", None), ("12345", None), ("56789", None)])
def test_given_not_int_proc_barcode_generates_exception(test_input, expected):
    """This test case checks none int parameter inputs.
    """
    with pytest.raises(TypeError):
        assert proc_barcode(test_input) is expected

@pytest.mark.parametrize("test_input,expected", [(54321, "Error: barcode not found"), (99999, "Error: barcode not found"), (11111, "Error: barcode not found")])
def test_given_wrong_barcode_proc_barcode_returns_err_msg(test_input, expected):
    """This test case checks if barcodes not known return None

    Args:
        test_input (_type_): input value
        expected (_type_): expected result
    """
    assert proc_barcode(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(12345, "$7.25"), (23456, "$12.50"), (45456, "$5.25")])
def test_given_right_barcode_proc_barcode_returns_value(test_input, expected):
    """This test case checks if barcodes not known return None

    Args:
        test_input (_type_): input value
        expected (_type_): expected result
    """
    assert proc_barcode(test_input) == expected

def test_empty_price_list_get_total_returns_zero(clean_totals):
    """This test case checks if the total calculation returns
        "$0.00" as value
    """
    #get_total() # this should clean all prices in the totals
    
    assert get_total() == "$0.00"

def test_given_wrong_barcodes_get_totals_returns_zero(clean_totals):
    """This test case checks that the totals calculation is
        returning "$0.00" if wrong barcodes are given
    """
    proc_barcode(121212)
    proc_barcode(121211)
    proc_barcode(121210)
    assert get_total() == "$0.00"

def test_given_right_barcodes_get_totals_return_corr_val(prep_25_dollars):
    """This test case checks that all known barcodes given
        generate the right output
    """
    assert get_total() == "$25.00"

def test_given_barcodes_get_totals_reset_the_totals(prep_25_dollars):
    """This test case checks that after reading the totals
        the total price is set to "$0.00"
    """
    assert get_total() == "$25.00"
    assert get_total() == "$0.00"
