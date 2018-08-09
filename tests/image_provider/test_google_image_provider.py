from itertools import combinations
import pytest

from nachbarstrom.commons.image_provider.google_image_provider import MapType, \
    GoogleImageProvider
from nachbarstrom.commons.world import Location

GERMANY_LOCATION = Location(48.193926, 11.621544)


@pytest.mark.integration
def test_different_maptypes_are_different():
    images = []
    for map_type in MapType:
        image_provider = GoogleImageProvider(map_type=map_type, zoom=17)
        images.append(image_provider.get_image_from(GERMANY_LOCATION))

    for image1, image2 in combinations(images, r=2):
        assert image1 != image2
