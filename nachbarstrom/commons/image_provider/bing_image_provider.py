import os
from urllib import request

from PIL import Image

from nachbarstrom.commons.world import Location, SquareAroundCenterLocation
from .image_provider import ImageProvider


class BingImageProvider(ImageProvider):

    DEFAULT_IMG_SIZE = 640

    def __init__(self, api_key: str = None, size: int = DEFAULT_IMG_SIZE):
        assert isinstance(size, int)

        if api_key is None:
            api_key = os.environ["BING_MAPS_KEY"]

        self._query_template = "https://dev.virtualearth.net/REST/v1/" \
                               "Imagery/Map/Aerial?" \
                               "mapArea={bottom:f},{left:f},{up:f},{right:f}" \
                               f"&mapSize={size},{size}" \
                               "&dpi=Large" \
                               f"&key={api_key}"

    def get_image_from(self, location: Location) -> Image:
        self._validate_input_format(location)
        query = self._format_query(location)
        image = Image.open(request.urlopen(query))
        self._validate_output_format(image)
        return image

    def _format_query(self, location: Location) -> str:
        square = SquareAroundCenterLocation(location)
        map_area_params = {
            "bottom": square.bottom_left_location.latitude,
            "left": square.bottom_left_location.longitude,
            "up": square.upper_right_location.latitude,
            "right": square.upper_right_location.longitude,
        }
        return self._query_template.format(**map_area_params)
