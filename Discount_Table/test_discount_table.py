import pytest

from .discount_table import discount_table

@pytest.mark.parametrize("price, expected", [
    ([4.95, 9.95, 14.95, 19.95, 24.95], (
    "Original:\t{:.2f}\tDiscount:\t{:.2f}\tNew:\t{:.2f}".format(4.95, 2.97, 1.98) +
    "\nOriginal:\t{:.2f}\tDiscount:\t{:.2f}\tNew:\t{:.2f}".format(9.95, 5.97, 3.98) +
    "\nOriginal:\t{:.2f}\tDiscount:\t{:.2f}\tNew:\t{:.2f}".format(14.95, 8.97, 5.98)  +
    "\nOriginal:\t{:.2f}\tDiscount:\t{:.2f}\tNew:\t{:.2f}".format(19.95, 11.97, 7.98) +
    "\nOriginal:\t{:.2f}\tDiscount:\t{:.2f}\tNew:\t{:.2f}\n".format(24.95, 14.97, 9.98)))
])
def test_discount_table(price, expected, capsys):
    discount_table(price)
    out, err = capsys.readouterr()
    assert out == expected

    