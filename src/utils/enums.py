
"""This module defines various enumerations used throughout the application.
"""
import datetime as dt
from enum import Enum, Flag, auto


class Weekday(Enum):
    """Enum representing the days of the week."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    # Note: The values correspond to the isoweekday() method of datetime.date,
    # where Monday is 1 and Sunday is 7.

    @classmethod
    def from_date(cls, date: dt.date) -> 'Weekday':
        """Create a Weekday enum member from a datetime.date object."""
        return cls(date.isoweekday())


class WeekdayFlag(Flag):
    """Flag enum representing combinations of weekdays."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64


# In cases where the actual values of the members do not matter,
# you can save yourself some work and use auto() for the values:
class WeekdayAuto(Flag):
    """Flag enum using auto() for automatic value assignment."""
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
    WEEKEND = SATURDAY | SUNDAY
    WEEKDAYS = MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY
    WORKDAYS = WEEKDAYS | SATURDAY


class Color(Enum):
    """Enum representing basic colors."""
    RED = 1
    GREEN = 2
    BLUE = 3


def main():
    """Example usage of the enums defined in this module."""
    today = dt.date.today()
    weekday = Weekday.from_date(today)
    print(f"Today is: {weekday.name}")

    # Example of using WeekdayFlag
    weekend = WeekdayFlag.SATURDAY | WeekdayFlag.SUNDAY
    print(f"Weekend days: {weekend}")


if __name__ == "__main__":
    main()
