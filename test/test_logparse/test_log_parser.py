""" pytest module for log_parser

This module defines the tests for the logparser.py module. Further explains of
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
__contact__ = "GitHub"
__copyright__ = "Copyright 2023, WShield"
__credits__ = ["Real Python"]
__date__ = "2023/09/15"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Development"
__version__ = "0.0.1"

################################################################################
# Imports
import pytest
from src.logparse import log_parser

################################################################################
# Test Functions

def test_given_a_wrong_type_log_parser_will_raise_exept():
    """ Test Case to check for wrong calling atributes
    """

    with pytest.raises(TypeError):
        assert log_parser(1)
        assert log_parser(123.4)

def test_given_non_existing_file_log_parser_will_raise_value_exept():
    """ Test Case to check for file existing
    """

    with pytest.raises(ValueError):
        assert log_parser("not_exist_file.log")

def test_given_empty_file_log_parser_will_return_empty_dict(test_create_empty_file):
    """Test Case to check if log_parser can handle
        an empty file correct.
    """
    tmp_log_file = test_create_empty_file
    result = log_parser(tmp_log_file)
    assert result == {'CRITICAL': 0, 'DEBUG': 0, 'ERROR': 0, 'INFO': 0, 'WARNING': 0}

def test_given_log_file_with_only_info_msg_log_parser_will_return_info_in_dict(test_create_info_log_file):
    """Test Case to check if log_parser handle info messages.
    """
    tmp_log_file = test_create_info_log_file
    result = log_parser(tmp_log_file)
    assert result == {'CRITICAL': 0, 'DEBUG': 0, 'ERROR': 0, 'INFO': 10, 'WARNING': 0}

def test_given_log_file_wtih_one_each_log_parser_will_return_one_each(test_create_mixed_log_file):
    """Test Case to test all possible message types
    """

    tmp_log_file = test_create_mixed_log_file
    result = log_parser(tmp_log_file)
    assert result == {'CRITICAL': 1, 'DEBUG': 1, 'ERROR': 1, 'INFO': 1, 'WARNING': 1}

def test_given_log_file_wtih_all_log_parser_will_return_all(test_create_rand_log_file):
    """Test Case to test all possible message types
    """

    tmp_log_file = test_create_rand_log_file
    result = log_parser(tmp_log_file)
    assert result == {'CRITICAL': 1, 'DEBUG': 5, 'ERROR': 2, 'INFO': 2, 'WARNING': 5}
