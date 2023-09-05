#!/usr/bin/env python
""" Test Driven Development Test: Notes.

see: https://earthly.dev/blog/pytest-fixtures/ for more details.

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
__copyright__ = "Copyright 2023, WShield"
__credits__ = ["https://earthly.dev/blog/pytest-fixtures/"]
__date__ = "2023/09/05"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "Development"
__version__ = "0.0.1"

import pytest


def test_add_note(app_without_notes):
    result = app_without_notes.add_note("Test note 1")
    assert result == "Note added successfully"
    assert len(app_without_notes.notes_list) == 1
    assert app_without_notes.notes_list[0].content == "Test note 1"


def test_get_note(app_with_notes):
    result = app_with_notes.get_note(0)
    assert result == "Test note 1"


def test_get_note_index_error(app_without_notes):
    result = app_without_notes.get_note(0)
    assert result == "Index out of range"


def test_edit_note(app_with_notes):
    app_with_notes.edit_note(0, "Test note 1 edited")
    result = app_with_notes.get_note(0)
    assert result == "Test note 1 edited"


def test_edit_note_index_error(app_without_notes):
    result = app_without_notes.edit_note(0, "Test note 1 edited")
    assert result == "Index out of range"

def test_add_note_with_param(note_data, app_without_notes):
    input_value, expected_output = note_data
    result = app_without_notes.add_note(input_value)
    assert result == expected_output
    assert len(app_without_notes.notes_list) == 1
    assert app_without_notes.notes_list[0].content == input_value