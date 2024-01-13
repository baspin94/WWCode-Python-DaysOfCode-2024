from Day_02 import area

def test_area():
    """Calculate area of circle given a radius."""
    radius = 1
    result = area(radius)
    assert result == 3.14

    radius = 5
    result = area(radius)
    assert result == 78.54

    radius = 3.14
    result = area(radius)
    assert result == 30.97

    radius = 100
    result = area(radius)
    assert result == 31415.93