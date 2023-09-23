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
from pathlib import Path
import logging
import pytest
import os

################################################################################
# fixtures
@pytest.fixture()
def test_create_empty_file(tmp_path)->str:
    """Creates an empty file in the temporary folder
    Args:
        tmp_path (_type_): temporary folder
    Returns:
        str: path to file
    """

    tmp_dir = Path(tmp_path)
    tmp_dir = tmp_dir / "empty"
    tmp_dir.mkdir()
    tmp_dir = tmp_dir.resolve()
    tmp_file = tmp_dir / "hello.txt"

    with open(tmp_file, mode="w", encoding="utf-8") \
        as my_file:
        my_file.write("")
    return str(tmp_file)

@pytest.fixture()
def test_create_info_log_file(tmp_path)->str:
    """Returns a log file with info log messages

    Args:
        tmp_path (_type_): temporary folder

    Returns:
        str: path to file
    """
    log_file = os.path.join(os.path.dirname(__file__), 'info.txt')
    return str(log_file)

@pytest.fixture()
def test_create_mixed_log_file(tmp_path)->str:
    """Returns a log file with all kinds of log messages

    Args:
        tmp_path (_type_): temporary folder

    Returns:
        str: path to file
    """
    log_file = os.path.join(os.path.dirname(__file__), 'mixed.txt')
    return str(log_file)

@pytest.fixture()
def test_create_rand_log_file(tmp_path)->str:
    """Returns a log file with all kinds of log messages

    Args:
        tmp_path (_type_): temporary folder

    Returns:
        str: path to file
    """
    log_file = os.path.join(os.path.dirname(__file__), 'rand.txt')
    return str(log_file)