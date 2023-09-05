import pytest
from src.notes_app import NotesApp

@pytest.fixture
def app():
    """Returns an instance of the NotesApp class."""
    app_obj = NotesApp()
    return app_obj

@pytest.fixture
def app_without_notes(app):
    return app


@pytest.fixture(scope="function")
def app_with_notes(app):
    """Returns an instance of the NotesApp class with two notes."""
    print("Setting up the data for the test...")
    app.add_note("Test note 1")
    app.add_note("Test note 2")
    print("Data is ready for the test...")
    yield app
    print("Cleaning up the data after the test...\n")
    app.notes_list = []


@pytest.fixture(params=[("Test note 1", "Note added successfully"),
                        ("Test note 2", "Note added successfully")])
def note_data(request):
    """Returns a tuple containing an input value and an expected \
    output value for the add_note method."""
    return request.param