from setuptools import setup

setup(
    name="nachbarstrom-commons",
    version="1.0",
    packages=[
        "nachbarstrom.commons.image_provider",
        "nachbarstrom.commons.world",
    ],
    install_requires="Pillow",
)
