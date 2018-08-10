from enum import Enum

import math


class RoofType(Enum):
    flat = 0
    gabled = 1
    halfHipped = 2
    hipped = 3
    mansard = 4
    pyramid = 5
    round = 6


class RoofOrientation(Enum):
    East = 0
    SouthEast = 1
    South = 2
    SouthWest = 3
    West = 4


class Roof:
    def __init__(self, roof_type: RoofType, orientation: RoofOrientation,
                 area: float) -> None:
        self._validate_input(roof_type, orientation, area)
        self.type = roof_type
        self.orientation = orientation
        self.area = float(area)

    @staticmethod
    def _validate_input(roof_type, orientation, area):
        assert roof_type is not None
        assert orientation is not None
        assert area is not None
        assert isinstance(roof_type, RoofType)
        assert isinstance(orientation, RoofOrientation)
        area = float(area)
        assert area >= 0

    def serialize(self):
        return {
            "roofType": self.type.name,
            "orientation": self.orientation.name,
            "area": str(self.area)
        }

    @staticmethod
    def from_dict(roof_details: dict):
        """
        Deserialize a Roof from a dict of the form:
        {
            "area: "100.00"
            "roofType": "hipped",
            "orientation": "SouthEast",
        }
        :param roof_details: the dict with the details
        :return: A Roof instance
        """
        assert "area" in roof_details
        assert "roofType" in roof_details
        assert "orientation" in roof_details
        return Roof(
            roof_type=RoofType[roof_details["roofType"]],
            orientation=RoofOrientation[roof_details["orientation"]],
            area=roof_details["area"],
        )

    def __eq__(self, other):
        return (self.type == other.type and
                self.orientation == other.orientation and
                math.isclose(self.area, other.area, rel_tol=1e-10))
