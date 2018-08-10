from enum import Enum


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
