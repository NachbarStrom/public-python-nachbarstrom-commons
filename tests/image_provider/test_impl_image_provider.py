from itertools import combinations
from typing import Sequence

import pytest
from PIL.Image import Image

from nachbarstrom.commons.image_provider import ImageProvider, \
    GoogleImageProvider, BingImageProvider
from nachbarstrom.commons.world import Location

GERMANY_LOCATION = Location(48.193926, 11.621544)


@pytest.fixture
def image_providers():
    return [GoogleImageProvider(), BingImageProvider()]


def test_validation_rejects_invalid_input(
        image_providers: Sequence[ImageProvider]):
    for provider in image_providers:
        invalid_inputs = [None, "invalid"]
        for invalid_input in invalid_inputs:
            with pytest.raises(AssertionError):
                provider.get_image_from(invalid_input)


@pytest.mark.integration
def test_output_is_pillow_image(image_providers: Sequence[ImageProvider]):
    for provider in image_providers:
        image = provider.get_image_from(GERMANY_LOCATION)
        assert isinstance(image, Image)


@pytest.mark.integration
def test_multiple_images_are_different(image_providers: Sequence[ImageProvider]):
    for provider in image_providers:
        images = _fetch_multiple_images(provider)
        for image1, image2 in combinations(images, r=2):
            assert image1 != image2


def _fetch_multiple_images(provider: ImageProvider):
    images = []
    for num in range(3):
        latitude = GERMANY_LOCATION.latitude + 0.01 * num
        location = Location(latitude, GERMANY_LOCATION.longitude)
        image = provider.get_image_from(location)
        images.append(image)
    return images
