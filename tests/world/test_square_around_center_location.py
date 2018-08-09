import pytest

from nachbarstrom.commons.world import Location, SquareAroundCenterLocation

INVALID_INPUTS = [None, 1, "string"]
VALID_LOCATION = Location(1.0, 1.0)


def test_construction_rejects_invalid_input_for_location():
    for invalid_input in INVALID_INPUTS:
        with pytest.raises(AssertionError):
            SquareAroundCenterLocation(center=invalid_input)


def test_construction_rejects_invalid_input_for_side_lenght():
    for invalid_input in INVALID_INPUTS:
        with pytest.raises(AssertionError):
            SquareAroundCenterLocation(VALID_LOCATION, invalid_input)


def test_object_contains_bottom_left_location():
    square = SquareAroundCenterLocation(VALID_LOCATION)
    assert isinstance(square.bottom_left_location, Location)


def test_object_contains_upper_right_location():
    square = SquareAroundCenterLocation(VALID_LOCATION)
    assert isinstance(square.upper_right_location, Location)
