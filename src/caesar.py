#!/usr/bin/env python
""" Short description of this Python module.

Caesar Cipher (caesar.py)

A Caesar cipher is a simple substitution cipher in which each letter of the 
plain text is substituted with a letter found by moving n places down the 
alphabet. For example, assume the input plain text is the following:

abcd xyz

If the shift value, n, is 4, then the encrypted text would be the following:
efgh bcd
You are to write a function that accepts two arguments, a plain-text message 
and a number of letters to shift in the cipher. The function will return an 
encrypted string with all letters transformed and all punctuation and whitespace 
remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII except for whitespace 
and punctuation.

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
__contact__ = "github"
__copyright__ = "Copyright 2023, WShield"
__credits__ = ["Real Python"]
__date__ = "2023/09/04"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Development"
__version__ = "0.0.1"

################################################################################
# Imports
import string
import logging
MSG_FORMAT = "%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=MSG_FORMAT)

################################################################################
# Variables

################################################################################
# Classes

################################################################################
# Functions

def caesar_cipher(plain_text:str, shift_num:int)->str:
    """Does a shift encryption of the given text.
    Args:
        plain_text (str): text to be encrypted
        shift_num (int): number of shifts
    Raises:
        TypeError: if wrong arguments handed over
    Returns:
        str: encrypted string
    """
    if not isinstance(plain_text, str) or not isinstance(shift_num, int):
        raise TypeError

    # prepare lower case translation table
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    lowercase_trantab = str.maketrans(letters, mask)
    # prepare upper case translation table
    letters = string.ascii_uppercase
    mask = letters[shift_num:] + letters[:shift_num]
    uppercase_trantab = str.maketrans(letters, mask)

    new_text = ""
    for single_char in plain_text:
        if single_char.islower():
            new_text = new_text + single_char.translate(lowercase_trantab)
        else:
            new_text = new_text + single_char.translate(uppercase_trantab)
    return new_text

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- any module script ---')
