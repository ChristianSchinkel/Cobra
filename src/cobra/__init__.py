"""Cobra package."""
from . import cli
from . import core
from . import utils

__all__ = [
    "cli",
    "core",
    "utils"
]  # Public API of the Cobra package

__author__ = ["Christian Schinkel"]  # Authors of the cli module
__version__ = "0.0.1"  # Version of the Cobra package
