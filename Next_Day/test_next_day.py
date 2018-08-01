import pytest
from .next_day import _print_date


@pytest.mark.parametrize("date, expected",[
    ("2013-12-31", "2014-01-01"),
    ("2014-2-28",   "2014-03-01"),
    ("2019-03-01",  "2019-03-02"),
    ("2000-05-30",  "2000-05-31"),
    ("3025-11-02",  "3025-11-03"),
    ("1945-07-22",  "1945-07-23"),
    ("685-07-31",  "685-08-01")
])
def test_next_day(date, expected):
    assert _print_date(date) == expected

