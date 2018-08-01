import pytest
from .reverse_order import reverse_order




@pytest.mark.parametrize("numbers, expected",[
    ("1 2 0 3", "3\n2\n1\n"),
    ("0", ""),
    ("0 0 0 0 0 1", "1\n")
])
def test_reverse_order(numbers, expected, capsys):
    reverse_order(numbers)
    out, err = capsys.readouterr()
    assert out == expected

