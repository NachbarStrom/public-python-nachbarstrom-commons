from nachbarstrom.commons.world import Location
from nachbarstrom.commons.image_provider import GoogleImageProvider

germany_location = Location(latitude=48.267991, longitude=11.665950)
img_provider = GoogleImageProvider()
satellite_img = img_provider.get_image_from(germany_location)
satellite_img.save("img.png")