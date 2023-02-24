import pytest
from src.pointsale import get_total, proc_barcode

@pytest.fixture()
def clean_totals():
    """This is a setup fixture to clean totals
    """
    get_total()
    yield
    get_total()

@pytest.fixture()
def prep_25_dollars():
    """This fixture cleans the totals and
        add barcodes with the value of 25$
    """

    get_total()
    proc_barcode(12345)
    proc_barcode(23456)
    proc_barcode(45456)
    yield
    get_total()