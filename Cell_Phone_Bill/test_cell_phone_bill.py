import pytest
from Cell_Phone_Bill.cell_phone_bill import cell_phone_bill



@pytest.mark.parametrize("minutes, texts, expected",[
    (51, 51, (
    "{:25} {:.2f}\n".format("Monthly rate:", 15.00) +
    "{:25} {:.2f}\n".format("Emergency support:", 0.44) +
    "{:25} {:.2f}\n".format("Additional minutes:", 0.25) +
    "{:25} {:.2f}\n".format("Additional texts:", 0.15) +
    "{:25} {:.2f}\n".format("Tax:", 0.77) +
    "{:25} {:.2f}".format("Total:", 16.61))
    ),
    (0, 0, (
    "{:25} {:.2f}\n".format("Monthly rate:", 15.00) +
    "{:25} {:.2f}\n".format("Emergency support:", 0.44) +
    "{:25} {:.2f}\n".format("Tax:", 0.77) +
    "{:25} {:.2f}".format("Total:", 16.21))
    ),
    (39, 39, (
    "{:25} {:.2f}\n".format("Monthly rate:", 15.00) +
    "{:25} {:.2f}\n".format("Emergency support:", 0.44) +
    "{:25} {:.2f}\n".format("Tax:", 0.77) +
    "{:25} {:.2f}".format("Total:", 16.21))
    ),
    (100, 100, (
    "{:25} {:.2f}\n".format("Monthly rate:", 15.00) +
    "{:25} {:.2f}\n".format("Emergency support:", 0.44) +
    "{:25} {:.2f}\n".format("Additional minutes:", 12.50) +
    "{:25} {:.2f}\n".format("Additional texts:", 7.50) +
    "{:25} {:.2f}\n".format("Tax:", 0.77) +
    "{:25} {:.2f}".format("Total:", 36.21))
    )
])
def test_cell_phone_bill(minutes, texts, expected):
    assert cell_phone_bill(minutes, texts) == expected

