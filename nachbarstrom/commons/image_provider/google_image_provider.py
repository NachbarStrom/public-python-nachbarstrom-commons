import os
from enum import Enum, auto
from urllib import request
from io import BytesIO
from PIL import Image

from nachbarstrom.commons.world import Location
from .image_provider import ImageProvider

GOOGLE_MAPS_KEY = os.environ["GOOGLE_MAPS_KEY"]


class MapType(Enum):
    roadmap = auto()
    satellite = auto()
    terrain = auto()
    hybrid = auto()


class GoogleImageProvider(ImageProvider):
    """Not thread-safe"""
    MIN_ZOOM = 0
    MAX_ZOOM = 21
    MAX_IMG_SIZE = 640

    def __init__(
            self,
            zoom: int = MAX_ZOOM,
            size: int = MAX_IMG_SIZE,
            api_key: str = GOOGLE_MAPS_KEY,
            map_type: MapType = MapType.satellite) -> None:
        assert self.MIN_ZOOM <= zoom <= self.MAX_ZOOM
        assert size <= self.MAX_IMG_SIZE
        self._image = None
        self._request_url = "https://maps.googleapis.com/maps/api/staticmap?" \
                            f"maptype={map_type.name}" \
                            "&center={latitude:f},{longitude:f}" \
                            f"&zoom={zoom}" \
                            f"&size={size}x{size}" \
                            f"&key={api_key}"

    def get_image_from(self, location: Location) -> Image.Image:
        self._validate_input_format(location)
        self._get_image(location)
        self._validate_output_format(self._image)
        return self._image

    def _get_image(self, location):
        url = self._fill_url(location)
        buffer = BytesIO(request.urlopen(url).read())
        self._image = Image.open(buffer)

    def _fill_url(self, location: Location):
        return self._request_url.format(
            latitude=location.latitude,
            longitude=location.longitude,
        )
