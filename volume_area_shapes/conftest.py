import pytest
from volume_area_shapes import Circle
from volume_area_shapes import Sphere
from volume_area_shapes import Rectangle
from volume_area_shapes import Cone


@pytest.fixture
def circle():
    return Circle

@pytest.fixture
def sphere():
    return Sphere

@pytest.fixture
def diameter():
    return 8

@pytest.fixture
def rectangle():
    return Rectangle

@pytest.fixture
def cone():
    return Cone


