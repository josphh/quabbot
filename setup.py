from os import path

from setuptools import find_packages, setup

__version__ = "0.0.1"


# Read long description from README.md
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name="quabbot",
    version=__version__,
    description="The Discord Companion and RPG Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/josphh/ribbot",
    project_urls={
        "Bug Reports": "https://github.com/josphh/ribbot/issues",
        "Source": "https://github.com/josphh/ribbot",
    },
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=[
        "discord.py >=1.2.5,<2",
        "discord-py-slash-command >2,<3",
    ],
    entry_points={
        "console_scripts": [
            "ribbot=ribbot.main:launch",
        ],
    },
)
