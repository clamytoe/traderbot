"""
setup.py

Setup for installing the package.
"""
from setuptools import setup, find_packages
from pathlib import Path

import traderbot

VERSION = traderbot.__version__
AUTHOR = traderbot.__author__
EMAIL = traderbot.__email__

BASE_DIR = Path(__file__).resolve().parent
README = BASE_DIR.joinpath("README.md")

setup(
    name="traderbot",
    version=VERSION,
    description="Automatic Trading Bot built  with python to implement my trading strategy. (traderbot)",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/clamytoe/traderbot",
    author=AUTHOR,
    author_email=EMAIL,
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.13.3",
    ],
    keywords="python utility",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pytest"],
    license="MIT",
    entry_points={
        "console_scripts": [
            "traderbot=traderbot.app:main"
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/clamytoe/traderbot/issues',
        'Source': 'https://github.com/clamytoe/traderbot/',
    },
)
