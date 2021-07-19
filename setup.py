import re
from os import path

from setuptools import find_packages, setup

# Read long description from README.md
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()


# Read version from quabbot/__init__.py
with open("quabbot/__init__.py", "r") as init_py:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', init_py.read(), re.MULTILINE
    ).group(1)


setup(
    name="quabbot",
    version=version,
    description="The Discord Companion and RPG Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/josphh/quabbot",
    project_urls={
        "Bug Reports": "https://github.com/josphh/quabbot/issues",
        "Source": "https://github.com/josphh/quabbot",
    },
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=[
        "discord.py >=1.2.5,<2",
        "discord-py-slash-command >2,<3",
        "jsons >=1,<2",
    ],
    entry_points={
        "console_scripts": [
            "quabbot=quabbot.main:launch",
        ],
    },
)
