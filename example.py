from nachbarstrom.commons.world import Location
from nachbarstrom.commons.image_provider import GoogleImageProvider

GERMANY_LOCATION = Location(latitude=48.267991, longitude=11.665950)
IMG_PROVIDER = GoogleImageProvider()
SATELLITE_IMG = IMG_PROVIDER.get_image_from(GERMANY_LOCATION)
SATELLITE_IMG.save("img.png")
