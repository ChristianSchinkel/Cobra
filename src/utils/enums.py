
"""This module defines various enumerations used throughout the application.
"""
from enum import Enum


class Weekday(Enum):
    """Enum representing the days of the week."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Color(Enum):
    """Enum representing basic colors."""
    RED = 1
    GREEN = 2
    BLUE = 3
