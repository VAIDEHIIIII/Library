import pytest
from fine import calculate_fine


@pytest.mark.parametrize("days, expected", [
    (0, 0),       # Zero days
    (2, 4),       # Valid input
    (5, 10),      # Boundary input
    (6, 15),      # Above boundary
    (10, 35)      # Valid input
])
def test_calculate_fine(days, expected):
    assert calculate_fine(days) == expected


@pytest.mark.parametrize("days", [
    -1,
    -5,
    2.5,
    "abc"
])
def test_invalid_days(days):
    with pytest.raises(ValueError):
        calculate_fine(days)