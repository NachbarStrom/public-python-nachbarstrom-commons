import pytest

from nachbarstrom.commons.world import RoofType, RoofOrientation, Roof

VALID_ROOF_AREA = 10.0
VALID_ROOF_ORIENTATION = RoofOrientation.South
VALID_ROOF_TYPE = RoofType.flat
VALID_ROOF = Roof(
    roof_type=VALID_ROOF_TYPE,
    orientation=VALID_ROOF_ORIENTATION,
    area=VALID_ROOF_AREA,
)
SERIALIZED_ROOF = {
    "roofType": "flat",
    "orientation": "South",
    "area": str(VALID_ROOF_AREA)
}


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
    assert SERIALIZED_ROOF == VALID_ROOF.serialize()


def test_from_dict_constructor():
    roof = Roof.from_dict(SERIALIZED_ROOF)
    assert roof == VALID_ROOF


def test_roundtrip_serialization():
    roof = Roof.from_dict(VALID_ROOF.serialize())
    assert roof == VALID_ROOF
