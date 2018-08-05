[![Build Status](https://travis-ci.org/NachbarStrom/public-python-nachbarstrom-commons.svg?branch=master)](https://travis-ci.org/NachbarStrom/public-python-nachbarstrom-commons)
[![codecov](https://codecov.io/gh/NachbarStrom/public-python-nachbarstrom-commons/branch/master/graph/badge.svg)](https://codecov.io/gh/NachbarStrom/public-python-nachbarstrom-commons)

# python-nachbarstrom-commons
Library of common python utils used by different NachbarStrom services

# Installation
````bash
cd python-nachbarstrom-commons
pip install .
````
# Usage
Set your api key as an environment variable
````bash
$ export GOOGLE_MAPS_KEY='your key here'
````
Example:
````python
from nachbarstrom.commons.world import Location
from nachbarstrom.commons.image_provider import GoogleImageProvider

germany_location = Location(latitude=48.0, longitude=11.0)
img_provider = GoogleImageProvider()
satellite_img = img_provider.get_image_from(germany_location)
````
