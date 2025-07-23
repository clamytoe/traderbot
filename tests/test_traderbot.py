"""
test_traderbot.py

Tests for traderbot.
"""
from os import environ
from dotenv import load_dotenv
from traderbot import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_env():
    load_dotenv()
    assert environ.get("TEST_VALUE") == "clamytoe"
