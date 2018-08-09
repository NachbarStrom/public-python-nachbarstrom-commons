import pytest

from nachbarstrom.commons.world import RoofType, RoofOrientation, Roof

VALID_ROOF_TYPE = RoofType.FLAT
VALID_ROOF_ORIENTATION = RoofOrientation.SOUTH


def test_constructor_rejects_none_input():
    valid_roof_area = 1.0

    with pytest.raises(AssertionError):
        Roof(None, VALID_ROOF_ORIENTATION, valid_roof_area)

    with pytest.raises(AssertionError):
        Roof(VALID_ROOF_TYPE, None, valid_roof_area)

    with pytest.raises(AssertionError):
        Roof(VALID_ROOF_TYPE, VALID_ROOF_ORIENTATION, None)


def test_constructor_rejects_negative_area():
    invalid_area = "-1.0"
    with pytest.raises(AssertionError):
        Roof(VALID_ROOF_TYPE, VALID_ROOF_ORIENTATION, invalid_area)


def test_constructor_rejects_invalid_area():
    invalid_area = "invalid"
    with pytest.raises(ValueError):
        Roof(VALID_ROOF_TYPE, VALID_ROOF_ORIENTATION, invalid_area)


def test_serialize():
    roof = Roof(
        RoofType.FLAT,
        RoofOrientation.SOUTH,
        10.0
    )
    expected_serialized_roof = {
        "roofType": "FLAT",
        "orientation": "SOUTH",
        "area": "10.0"
    }
    assert expected_serialized_roof == roof.serialize()
