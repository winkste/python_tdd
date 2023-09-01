""" List files in a directory including all sub directories

List Files

Function to list all files in a sub directory given a parent
folder.

Prerequisites


Requirements
1. If function argument is not given, not a string raise TypeError

2. If the function argument is not a valid folder, return None

For example "root-folder"

root-folder
    -> folder
        -> file.txt
        -> file2.txt

    return: ["root-folder/folder", "root-folder/folder/file.txt", "root-folder/folder/file2.txt"]

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
################################################################################
# Variables
################################################################################
# Functions

def list_files(root_dir:str):
    """ This function list all elements of a root directory
    """
    if root_dir == "":
        raise TypeError
    if not isinstance(root_dir, str):
        raise TypeError
    return None

################################################################################
# Classes
################################################################################
# Scripts
#if __name__ == "__main__":
#    # execute only if run as a script
#    print('--- any module script ---')


