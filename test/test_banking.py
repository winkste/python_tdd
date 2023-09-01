#!/usr/bin/env python
""" Test Driven Development Test: banking.

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

from datetime import date
import pytest
from src.banking import Account

class TestBanking:
    @pytest.mark.parametrize(
        "test_input,expected", [("Not Int", None), ("12345", None), ("56789", None)]
    )
    def test_given_not_int_deposit_raise_except(self, test_input, expected):
        """This test case checks none int parameter inputs."""
        bank = Account()

        with pytest.raises(TypeError):
            assert bank.deposit(test_input) is expected


    @pytest.mark.parametrize("test_input,expected", [(-100, None), (0, None), (-200, None)])
    def test_given_bad_int_deposit_raise_exept(self, test_input, expected):
        """This test case checks bad integer values"""
        bank = Account()
        with pytest.raises(ValueError):
            assert bank.deposit(test_input) is expected


    @pytest.mark.parametrize("test_input,expected", [(100, None), (1, None), (200, None)])
    def test_given_amount_deposit_is_returning_none(self, test_input, expected):
        """This test case checks good inputs"""
        bank = Account()
        assert bank.deposit(test_input) is expected


    def test_given_empty_account_print_statement_returns_empty(self, capsys):
        """This test case checks that the initial account statement
        is empty.
        """
        bank = Account()
        bank.print_statement()
        capture = capsys.readouterr()
        today = date.today().strftime("%d/%m/%Y")
        expected_statement = f"DATE|AMOUNT|BALANCE\n{today}|-|0.00\n"
        assert capture.out.strip() == expected_statement.strip()


    def test_given_300_print_statement_returns_300(self, capsys):
        """This test case checks if 300 is deposed that the account
        statement prints 300
        """
        bank = Account()
        bank.deposit(300)
        bank.print_statement()
        capture = capsys.readouterr()
        today = date.today().strftime("%d/%m/%Y")
        expected_statement = f"DATE|AMOUNT|BALANCE\n{today}|-|0.00\n{today}|300.00|300.00\n"
        assert capture.out == expected_statement


    def test_given_multi_deposits_print_statement_returns_multi(self, capsys):
        """This test case checks multiple deposits and at the
        end the right bank statement
        """
        bank = Account()
        bank.deposit(300)
        bank.deposit(100)
        bank.deposit(500)
        bank.deposit(300)
        bank.print_statement()
        capture = capsys.readouterr()
        # dd/mm/YY
        today = date.today().strftime("%d/%m/%Y")
        expected_statement = f"""DATE|AMOUNT|BALANCE
{today}|-|0.00
{today}|300.00|300.00
{today}|100.00|400.00
{today}|500.00|900.00
{today}|300.00|1200.00
"""
        assert capture.out == expected_statement


    @pytest.mark.parametrize(
        "test_input,expected", [("Not Int", None), ("12345", None), ("56789", None)]
    )
    def test_given_not_int_withdraw_raise_except(self, test_input, expected):
        """This test case checks withdraw against wrong input types"""

        bank = Account()

        with pytest.raises(TypeError):
            assert bank.withdraw(test_input) is expected


    @pytest.mark.parametrize("test_input,expected", [(-100, None), (0, None), (-200, None)])
    def test_given_bad_int_withdraw_raise_exept(self, test_input, expected):
        """This test case checks bad integer values"""
        bank = Account()
        with pytest.raises(ValueError):
            assert bank.withdraw(test_input) is expected

    def test_calling_withdraw_without_balance_returns_zero(self):
        """This test case checks if the withdraw returns zero if balance is
        lower the withdraw value """
        bank = Account()

        assert bank.withdraw(100) == 0
        bank.deposit(100)
        assert bank.withdraw(150) == 0

    def test_withdraw_with_balance_will_return_withdraw(self):
        """This test case checks that if a valid value is withdrawn
        and the balance is high enough, the withdrawn value is returned"""

        bank = Account()

        bank.deposit(100)
        assert bank.withdraw(100) == 100

    def test_withdraw_with_balance_will_reduce_balance(self, capsys):
        """This test case checks the balance sheet after withdraw"""
        bank = Account()
        bank.deposit(100)
        bank.withdraw(100)
        bank.print_statement()
        capture = capsys.readouterr()
        # dd/mm/YY
        today = date.today().strftime("%d/%m/%Y")
        expected_statement = f"""DATE|AMOUNT|BALANCE
{today}|-|0.00
{today}|100.00|100.00
{today}|-100.00|0.00
"""
        assert capture.out == expected_statement
