import pytest
from Fuel_Efficiency import mpg_lkm

@pytest.fixture(scope="module")
def conversion():
    return mpg_lkm

@pytest.mark.parametrize("mpg, expected",[
    (20, 11.76),
    (30, 7.84)
    ])
def test_mpg_lkm(conversion, mpg, expected):
    """test MPG converts to L per 100 km"""
    assert round(conversion(mpg), 2) == expected




