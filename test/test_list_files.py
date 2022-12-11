#!/usr/bin/env python
""" Test driven development of list file module

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
__credits__ = ["Martin C. Roberts"]
__date__ = "2022/12/10"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

################################################################################
# Imports
import os

import pytest
from src.listfiles import list_files

################################################################################
# Variables
################################################################################
# Functions
def test_given_not_string_list_files_will_raise_type_error():
    """ This function tests if list_files raises TypeError when not string arg
    """
    with pytest.raises(TypeError):
        list_files(123)
        list_files(1.2)

def test_given_empty_string_list_files_will_raise_type_error():
    """ This function tests if list_files raises TypeError when when empty string
    """
    with pytest.raises(TypeError):
        list_files("")

def test_given_not_valid_folder_list_files_will_return_none():
    """ This function tests if list_files returns none if not a valid folder is
        given
    """
    assert list_files("This is nothing") is None

def test_given_a_file_path_list_files_will_return_none(tmpdir):
    """ This function tests if list_files returns none if file path given
    """
    print("This is my test")
    test_file = tmpdir.mkdir("subdir").join("test1.txt")
    test_file.write("This is temp test")

    #print(tmpdir)
    print(test_file.basename)
    #print(test_file.dirname)
    print(test_file.dirname + test_file.basename)
    assert list_files(test_file.dirname + "/" + test_file.basename) is None

################################################################################
# Classes
################################################################################
# Scripts
