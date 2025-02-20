import pytest


@pytest.fixture
def mock_package_measurements():
    return [
        (50, 50, 50, 10, "STANDARD"),
        (200, 50, 50, 10, "SPECIAL"),
        (50, 50, 50, 25, "SPECIAL"),
        (200, 50, 50, 25, "REJECTED"),
        (150, 10, 10, 10, "SPECIAL"),
        (100, 100, 50, 30, "SPECIAL"),
        (200, 200, 200, 5, "SPECIAL"),
    ]