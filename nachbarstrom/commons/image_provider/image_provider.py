from PIL import Image
from typeguard import typechecked

from nachbarstrom.commons.world import Location


class ImageProvider:
    """Provides satellite images."""

    def get_image_from(self, location: Location) -> Image.Image:
        """
        Get a satellite image.
        :param location: The location at the center of the Image.
        :return: The satellite image in Pillow format.
        """
        raise NotImplementedError


class MockImageProvider(ImageProvider):

    @typechecked
    def get_image_from(self, location: Location) -> Image:
        return Image.new("RGB", (10, 10))
