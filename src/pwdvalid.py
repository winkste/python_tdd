#!/usr/bin/env python
""" Test Driven Development Kata4: Password validation.

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

import re

def validate_pwd(pwd_str:str):
    """
        This function validates a password. Requirements:
        1. The password must be at least 8 characters long. If it is not met, then the
        following error message should be returned: “Password must be at least 8 characters”

        2. The password must contain at least 2 numbers. If it is not met, then the following
        error message should be returned: “The password must contain at least 2 numbers”

        3. The validation function should handle multiple validation errors.

        For example, “somepassword” should an error message: “Password must be at least 8 characters
        The password must contain at least 2 numbers”
        4. The password must contain at least one capital letter. If it is not met,
        then the following error message should be returned: “password must contain at
        least one capital letter”

        5. The password must contain at least one special character. If it is not met,
        then the following error message should be returned: “password must contain at
        least one special character”

    """
    err_str:str     = ""


    if not isinstance(pwd_str, str):
        raise TypeError

    if len(pwd_str) < 8:
        err_str += " Password must be at least 8 characters"

    # using regex to check if two digits are in the password
    if len(re.sub('[^\\d]' , '', pwd_str)) < 2:
        err_str += " The password must contain at least 2 numbers"

    # Using regex to check for any element to be uppercase
    if not bool(re.match(r'\w*[A-Z]\w*', pwd_str)):
        err_str += " Password must contain at least one capital letter"

    # Using regex to check for any special character in string
    regex = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')
    if regex.search(pwd_str) is None:
        err_str += " Password must contain at least one special character"


    return len(err_str) == 0, err_str
