#!/usr/bin/env python
""" Log Parser (logparse.py)

Accepts a filename on the command line. The file is a Linux-like log file
from a system you are debugging. Mixed in among the various statements are
messages indicating the state of the device. They look like this:

Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON

The device state message has many possible values, but this program cares
about only three: ON, OFF, and ERR.
This program will parse the given log file and print out a report giving
how long the device was ON and the timestamp of any ERR conditions.
Example:
    ./logparse.py test.log
    Device was on for 7 seconds
    Timestamps of error events:
    Jul 11 16:11:54:661
    Jul 11 16:11:56:067

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
import logging
MSG_FORMAT = "%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s"
LOG_FILE = 'example.log'
LOG_LEVEL=logging.DEBUG
logging.basicConfig(filename=LOG_FILE, encoding="utf-8", level=LOG_LEVEL, format=MSG_FORMAT)

import os
################################################################################
# Variables

################################################################################
# Classes

################################################################################
# Functions

def log_parser(log_file:str)->dict:
    """Parser for log lessage files

    Args:
        log_file (str): path to log file

    Returns:
        dict: dictionary with log file statistics
    """

    # validate the input parameters first
    check_input_parameter(log_file)

    # prepare the statistics dictionary
    cnt_dict = {}
    cnt_dict["DEBUG"] = 0
    cnt_dict["INFO"] = 0
    cnt_dict["WARNING"] = 0
    cnt_dict["ERROR"] = 0
    cnt_dict["CRITICAL"] = 0

    # Open the file with closing at the ned
    with open(log_file, encoding="utf-8") as my_file:
        for line in my_file:
            for key in cnt_dict:
                if key in line:
                    cnt_dict[key] = cnt_dict[key] + 1
    return cnt_dict

def check_input_parameter(log_file:str)->None:
    """Checks the input parameter

    Args:
        log_file (str): path to log file

    Raises:
        TypeError: if log file path not a string
        ValueError: if log file not a file
    """
    if not isinstance(log_file, str):
        raise TypeError

    if not os.path.isfile(log_file):
        raise ValueError

################################################################################
# Scripts
