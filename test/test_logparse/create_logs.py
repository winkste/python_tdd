#!/usr/bin/env python
""" Script to create the log files

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
__contact__ = "GitHub"
__copyright__ = "Copyright 2023, WShield"
__date__ = "2023/09/21"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Development"
__version__ = "0.0.1"


################################################################################
# Imports
import logging
from pathlib import Path
import os

################################################################################
# Variables

################################################################################
# Classes

################################################################################
# Functions

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script

    log_file = os.path.join(os.path.dirname(__file__), 'rand.txt')
    msg_format = "%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s"
    log_level=logging.DEBUG
    logging.basicConfig(filename=log_file, encoding="utf-8", level=log_level, format=msg_format)

    logging.info('This is an info message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.info('This is an info message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
