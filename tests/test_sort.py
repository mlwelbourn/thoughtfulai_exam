from thoughtful_exam import sort


def test_sort(mock_package_measurements):
    for width, height, length, mass, expected in mock_package_measurements:
        assert sort(width, height, length, mass) == expected, f"Failed for ({width}, {height}, {length}, {mass})"