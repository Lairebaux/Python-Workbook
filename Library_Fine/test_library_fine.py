import pytest
from .Library_Fine import library_fine



@pytest.mark.parametrize("d1, m1, y1, d2, m2, y2, expected", [
    (2, 1, 2018, 1, 1, 2018, 15),
    (25, 12, 2018, 26, 12, 2000, 10000),
    (5, 6, 2015, 6, 6, 2015, 0),
    (14, 4, 2099, 13, 4, 2099, 15),
])
def test_library_fine(d1, m1, y1, d2, m2, y2, expected):
    assert library_fine(d1, m1, y1, d2, m2, y2) == expected


