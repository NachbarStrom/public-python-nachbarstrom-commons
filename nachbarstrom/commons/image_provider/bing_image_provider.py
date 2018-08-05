import os
from urllib import request

from PIL import Image

from nachbarstrom.commons.world import Location, SquareAroundCenterLocation
from .image_provider import ImageProvider

BING_MAPS_KEY = os.environ["BING_MAPS_KEY"]


class BingImageProvider(ImageProvider):
    _QUERY_TEMPLATE = "https://dev.virtualearth.net/REST/v1/" \
                      "Imagery/Map/Aerial?" \
                      "mapArea={bottom},{left},{up},{right}" \
                      "&mapSize={size},{size}" \
                      "&dpi=Large" \
                      "&key={bing_maps_key}"
    _FLOAT_FORMAT = "{:.6f}"

    def __init__(self, size: int=400):
        self._size = size

    def get_image_from(self, location: Location) -> Image:
        self._validate_input_format(location)
        query = self._format_query(location)
        image = Image.open(request.urlopen(query))
        self._validate_output_format(image)
        return image

    def _format_query(self, location: Location) -> str:
        params = {
            "bing_maps_key": BING_MAPS_KEY,
            "lat": self._get_float_string(location.latitude),
            "lon": self._get_float_string(location.longitude),
            "size": self._size,
        }
        square_params = self._get_square_params_around(location)
        params.update(square_params)
        return self._QUERY_TEMPLATE.format(**params)

    def _get_float_string(self, float_: float) -> str:
        return self._FLOAT_FORMAT.format(float_)

    def _get_square_params_around(self, location: Location) -> dict:
        square = SquareAroundCenterLocation(location)
        square_params = {
            "bottom": square.bottom_left_location.latitude,
            "left": square.bottom_left_location.longitude,
            "up": square.upper_right_location.latitude,
            "right": square.upper_right_location.longitude
        }
        return {k: self._get_float_string(v) for k, v in square_params.items()}
