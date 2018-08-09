import pytest
from PIL.Image import Image

from nachbarstrom.commons.image_provider import MockImageProvider
from nachbarstrom.commons.world import Location


@pytest.fixture
def mock_image_provider():
    return MockImageProvider()


def test_image_from(mock_image_provider: MockImageProvider):
    location = Location(latitude=0.0, longitude=0.0)
    image = mock_image_provider.get_image_from(location)
    assert isinstance(image, Image)
