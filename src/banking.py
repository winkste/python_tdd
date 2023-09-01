#!/usr/bin/env python
""" Test Driven Development Kata 6: Banking kata
Note: This is an advanced example where the solution requires knowledge
of using a mocking framework. The possible solution can also have an elaborated
design. Solve it only if you feel comfortable with mocking frameworks and
designing your code.

Create a simple bank application with features of depositing, withdrawing,
and printing account statements.

Constraints

1. Start with a class with the following structure

class Account
{
  public void deposit(int amount)
  public void withdraw(int amount)
  public void printStatement()
}
2. You are not allowed to add any other public methods in this class

3. Use Strings and Integers for dates and amounts (keep it simple)

4. Don’t worry about the spacing in the statement printed in the console

Requirements

1. Deposit into Account

2. Withdraw from an Account

3. Print the Account statement to the console

DATE       | AMOUNT  | BALANCE
10/04/2014 | 500.00  | 1400.00
02/04/2014 | -100.00 | 900.00
01/04/2014 | 1000.00 | 1000.00

Reference: https://tddmanifesto.com/exercises/


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

################################################################################
# Imports
from datetime import date

################################################################################
# Variables

################################################################################
# Functions

################################################################################
# Classes
class Account:
    """This class handles the account
    """
    def __init__(self):
        """This is the class init funciton
        """
        self.balance:float = 0.00
        self.bal_cheet:list = ["DATE|AMOUNT|BALANCE"]
        self._append_balance_sheet(0)

    def deposit(self, amount:int)->None:
        """This function adds amount to account

        Args:
            amount (int): amount to add to account
        """
        self._check_amount_input(amount)

        self.balance += amount
        self._append_balance_sheet(amount)

    def _append_balance_sheet(self, amount:int)->None:
        """This function add an entry to the balance sheet

        Args:
            amount (int): the amount that have been deposit or withdrawn
        """
        if amount != 0:
            amount_str = f"{amount:.2f}"
        else:
            amount_str = "-"

        # dd/mm/YY
        today = date.today().strftime("%d/%m/%Y")
        self.bal_cheet.append(f"{today}|{amount_str}|{self.balance:.2f}")

    def _check_amount_input(self, amount:int)->None:
        """_summary_

        Args:
            amount (int): amount input
        """
        if isinstance(amount, int) is False:
            raise TypeError("Amount not a number.")

        if 0 >= amount:
            raise ValueError("Amount needs to be >= 0")

    def print_statement(self)->None:
        """This function prints the statement.
        """
        for line in self.bal_cheet:
            print(line)

    def withdraw(self, amount:int)->int:
        """This function withdraws the amount of money if balance
            is sufficient.

        Args:
            amount (int): amount of money to withdraw

        Returns:
            int: amount if balance is available, else 0
        """
        self._check_amount_input(amount)

        if self.balance >= amount:
            self.balance -= amount
            self._append_balance_sheet(-amount)

            return amount

        return 0

################################################################################
# Scripts
#if __name__ == "__main__":
#    # execute only if run as a script
#    print('--- any module script ---')
#    bank = Account()
#    bank.deposit(100)
#    bank.withdraw(100)
#    bank.print_statement()
