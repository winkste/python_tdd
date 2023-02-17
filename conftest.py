import pytest
from src.pointsale import get_total

@pytest.fixture()
def clean_totals():
    """This is a setup fixture to clean totals
    """
    get_total()
    yield