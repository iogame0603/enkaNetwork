from setuptools import setup

setup(
    name="enkaNetwork",
    version="0.22",
    description="enka network to json library",
    install_requires=[
        "aiofiles==23.2.1",
        "aiohttp==3.8.4",
        "pydantic==2.6.3"
    ],
    package_data={"enkaNetwork": ["assets/*.json", "assets/hsr/*.json"]}
)