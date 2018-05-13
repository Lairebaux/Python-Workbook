
def test_circle_area(circle, diameter):
    """test area of a circle given its diameter"""
    assert circle(diameter).area() == '50.27'

def test_circle_circum(circle, diameter):
    """test area of a circle given its diameter"""
    assert circle(diameter).perimeter() == '25.13'

def test_sphere_area(sphere, diameter):
    """test area of a sphere given its diameter"""
    assert sphere(diameter).area() == '201.06'

def test_sphere_volume(sphere, diameter):
    """test volume of a sphere given its diameter"""
    assert sphere(diameter).volume() == '268.08'

def test_rectangle_area(rectangle):
    """test area of a rectangle given length, width"""
    assert rectangle(4, 5).area() == '20.00'

def test_rectangle_perimeter(rectangle):
    """test perimeter of a rectangle given length, width"""
    assert rectangle(4, 5).perimeter() == '18.00'

def test_rectangle_volume(rectangle):
    """test perimeter of a rectangle given length, width"""
    assert rectangle(4, 5, 6).volume() == '120.00'

def test_cone_area(cone, diameter):
    """test cone volume given length, width, height"""
    height, slant = 6, 3
    assert cone(diameter, height, slant).area() == '87.96'

def test_cone_volume(cone, diameter):
    """test cone volume given length, width, height"""
    height = 6
    assert cone(diameter, height).volume() == '100.53'

