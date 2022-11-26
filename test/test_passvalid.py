#!/usr/bin/env python
""" Test Driven Development Test: KATA4 password validator

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
from src.pwdvalid import validate_pwd

def test_given_not_string_validate_pwd_will_throw_typeerr():
    """
        This function will test that validate_pwd will check for
        types and throws typeerrror if not string.
    """
    with pytest.raises(TypeError):
        assert validate_pwd(123)
        assert validate_pwd(1.234)
        assert validate_pwd([1,2,3,4])

def test_given_strong_pwd_validate_pwd_will_give_true():
    """
        This function will check a strong pwd.
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("somePwd12$")
    assert val is True
    assert len(err_str) == 0

def test_given_zero_string_validate_pwd_will_give_false():
    """
        Test for empty password string.
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("")
    assert val is False
    assert len(err_str) >= 1
    assert err_str.find("Password must be at least 8 characters") != -1

def test_given_a_short_string_validate_pwd_will_give_false():
    """
        Test for short password string.
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("somepw1")
    assert val is False
    assert len(err_str) >= 1
    assert err_str.find("Password must be at least 8 characters") != -1

def test_given_a_pwd_wo_numbers_validate_pwd_will_give_number_error():
    """
        Test for numbers in password string.
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("somepw1")
    assert val is False
    assert len(err_str) >= 1
    assert err_str.find("The password must contain at least 2 numbers") != -1

def test_given_pwd_without_uppercase_validate_pwd_will_generate_error():
    """
        This function tests that a pwd without uppercase return error
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("somepw1")
    assert val is False
    assert len(err_str) >= 1
    assert err_str.find("Password must contain at least one capital letter") != -1

def test_given_pwd_wo_sepc_char_validate_pwd_will_give_error():
    """
        This function tests that a pwd without one special character will result in
        an error message
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("somepw1")
    assert val is False
    assert len(err_str) >= 1
    assert err_str.find("Password must contain at least one special character") != -1

def test_given_shortandonlyonedigitpwd_validate_pwd_will_give_multiple_errors():
    """
        This function will check for short and not two digit password
    """
    err_str:str
    val:bool

    val, err_str = validate_pwd("somepw1")
    assert val is False
    assert len(err_str) >= 1
    assert err_str.find("Password must be at least 8 characters") != -1
    assert err_str.find("The password must contain at least 2 numbers") != -1
    assert err_str.find("Password must contain at least one capital letter") != -1
    assert err_str.find("Password must contain at least one special character") != -1
