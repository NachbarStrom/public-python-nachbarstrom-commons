import os
from urllib import request

from PIL import Image
from typeguard import typechecked

from nachbarstrom.commons.world import Location
from .image_provider import ImageProvider


class BingImageProvider(ImageProvider):

    DEFAULT_IMG_PIXEL_SIZE = 640
    MAX_ZOOM_IN_MILES = 0.00275
    MIN_IMG_ZOOM = 1
    MAX_IMG_ZOOM = 21
    DEFAULT_IMG_ZOOM = MAX_IMG_ZOOM - 1  # Bing doesn't automatically
    # fallback to the next available size, so we have to be defensive.
    _API_KEY_ENV_VAR = "BING_MAPS_KEY"

    def __init__(
            self,
            api_key: str = None,
            size: int = DEFAULT_IMG_PIXEL_SIZE,
            zoom: int = DEFAULT_IMG_ZOOM):

        assert isinstance(size, int)
        assert self.MIN_IMG_ZOOM <= zoom <= self.MAX_IMG_ZOOM
        assert isinstance(zoom, int)

        if api_key is None:
            api_key = self._get_api_key()

        self._img_size = size
        self._query_template = "https://dev.virtualearth.net/REST/v1/" \
                               "Imagery/Map/Aerial" \
                               "/{latutude:f},{longitude:f}" \
                               f"/{zoom}" \
                               f"?mapSize={size},{size}" \
                               "&dpi=Large" \
                               f"&key={api_key}"

    def _get_api_key(self):
        assert self._API_KEY_ENV_VAR in os.environ, \
            f"The environment variable '{self._API_KEY_ENV_VAR}' is not set!"
        return os.environ[self._API_KEY_ENV_VAR]

    @typechecked
    def get_image_from(self, location: Location) -> Image.Image:
        query = self._format_query(location)
        image = Image.open(request.urlopen(query))
        return self._upsample_img_middle(image)

    def _format_query(self, location: Location) -> str:
        return self._query_template.format(
            latutude=location.latitude,
            longitude=location.longitude,
        )

    def _upsample_img_middle(self, image: Image.Image):
        corner_one = self._img_size / 4
        corner_two = self._img_size * 3 / 4
        box = (corner_one, corner_one, corner_two, corner_two)
        cropped_img = image.crop(box)
        usual_size = (self._img_size, self._img_size)
        return cropped_img.resize(usual_size)
