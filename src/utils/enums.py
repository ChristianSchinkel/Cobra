
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


class Switch(Enum):
    """Enum representing a simple on/off switch."""
    OFF = False
    ON = True


class GreekLetter(Enum):
    """Enum representing the first few Greek letters."""
    ALPHA = 1
    BETA = 2
    GAMMA = 3
    DELTA = 4
    EPSILON = 5
    ZETA = 6
    ETA = 7
    THETA = 8
    IOTA = 9
    KAPPA = 10
    LAMBDA = 11
    MU = 12
    NU = 13
    XI = 14
    OMICRON = 15
    PI = 16
    RHO = 17
    SIGMA = 18
    TAU = 19
    UPSILON = 20
    PHI = 21
    CHI = 22
    PSI = 23
    OMEGA = 24

    def kapitalize(self) -> str:
        """Return the name of the Greek letter in uppercase."""
        match self:
            case GreekLetter.ALPHA:
                return "A"
            case GreekLetter.BETA:
                return "B"
            case GreekLetter.GAMMA:
                return "Γ"
            case GreekLetter.DELTA:
                return "Δ"
            case GreekLetter.EPSILON:
                return "Ε"
            case GreekLetter.ZETA:
                return "Ζ"
            case GreekLetter.ETA:
                return "Η"
            case GreekLetter.THETA:
                return "Θ"
            case GreekLetter.IOTA:
                return "Ι"
            case GreekLetter.KAPPA:
                return "Κ"
            case GreekLetter.LAMBDA:
                return "Λ"
            case GreekLetter.MU:
                return "Μ"
            case GreekLetter.NU:
                return "Ν"
            case GreekLetter.XI:
                return "Ξ"
            case GreekLetter.OMICRON:
                return "Ο"
            case GreekLetter.PI:
                return "Π"
            case GreekLetter.RHO:
                return "Ρ"
            case GreekLetter.SIGMA:
                return "Σ"
            case GreekLetter.TAU:
                return "Τ"
            case GreekLetter.UPSILON:
                return "Υ"
            case GreekLetter.PHI:
                return "Φ"
            case GreekLetter.CHI:
                return "Χ"
            case GreekLetter.PSI:
                return "Ψ"
            case GreekLetter.OMEGA:
                return "Ω"

    def klower(self) -> str:
        """Return the name of the Greek letter in lowercase."""
        match self:
            case GreekLetter.ALPHA:
                return "a"
            case GreekLetter.BETA:
                return "b"
            case GreekLetter.GAMMA:
                return "γ"
            case GreekLetter.DELTA:
                return "δ"
            case GreekLetter.EPSILON:
                return "ε"
            case GreekLetter.ZETA:
                return "ζ"
            case GreekLetter.ETA:
                return "η"
            case GreekLetter.THETA:
                return "θ"
            case GreekLetter.IOTA:
                return "ι"
            case GreekLetter.KAPPA:
                return "κ"
            case GreekLetter.LAMBDA:
                return "λ"
            case GreekLetter.MU:
                return "μ"
            case GreekLetter.NU:
                return "ν"
            case GreekLetter.XI:
                return "ξ"
            case GreekLetter.OMICRON:
                return "ο"
            case GreekLetter.PI:
                return "π"
            case GreekLetter.RHO:
                return "ρ"
            case GreekLetter.SIGMA:
                return "σ"
            case GreekLetter.TAU:
                return "τ"
            case GreekLetter.UPSILON:
                return "υ"
            case GreekLetter.PHI:
                return "φ"
            case GreekLetter.CHI:
                return "χ"
            case GreekLetter.PSI:
                return "ψ"
            case GreekLetter.OMEGA:
                return "ω"


class GreekCountingWord(Enum):
    """Enum representing Greek counting words."""
    MONO = 1
    DI = 2
    TRI = 3
    TETRA = 4
    PENTA = 5
    HEXA = 6
    HEPTA = 7
    OKTA = 8
    NONA = 9
    DECA = 10
    UNDEKA = 11
    DODEKA = 12
    IKOSA = 20


class Prefix(Enum):
    """Enum representing common prefixes."""
    YOTTA = 1e24
    ZETTA = 1e21
    EXA = 1e18
    PETA = 1e15
    TERA = 1e12
    GIGA = 1e9
    MEGA = 1e6
    KILO = 1e3
    HECTO = 1e2
    DEKA = 1e1
    DECI = 1e-1
    CENTI = 1e-2
    MILLI = 1e-3
    MICRO = 1e-6
    NANO = 1e-9
    PICO = 1e-12
    FEMTO = 1e-15
    ATTO = 1e-18
    ZEPTO = 1e-21
    YOKTO = 1e-24

    def scale(self, value: float) -> float:
        """Scale a value by the prefix."""
        return value * self.value

    def descale(self, value: float) -> float:
        """Descale a value by the prefix."""
        return value / self.value

    def symbol(self) -> str:
        """Return the symbol for the prefix."""
        match self:
            case Prefix.YOTTA:
                return "Y"
            case Prefix.ZETTA:
                return "Z"
            case Prefix.EXA:
                return "E"
            case Prefix.PETA:
                return "P"
            case Prefix.TERA:
                return "T"
            case Prefix.GIGA:
                return "G"
            case Prefix.MEGA:
                return "M"
            case Prefix.KILO:
                return "k"
            case Prefix.HECTO:
                return "h"
            case Prefix.DEKA:
                return "da"
            case Prefix.DECI:
                return "d"
            case Prefix.CENTI:
                return "c"
            case Prefix.MILLI:
                return "m"
            case Prefix.MICRO:
                return "μ"
            case Prefix.NANO:
                return "n"
            case Prefix.PICO:
                return "p"
            case Prefix.FEMTO:
                return "f"
            case Prefix.ATTO:
                return "a"
            case Prefix.ZEPTO:
                return "z"
            case Prefix.YOKTO:
                return "y"


def main():
    """Example usage of the enums defined in this module."""
    today = dt.date.today()
    weekday = Weekday.from_date(today)
    print(f"Today is: {weekday.name}")

    # Example of using WeekdayFlag
    weekend = WeekdayFlag.SATURDAY | WeekdayFlag.SUNDAY
    print(f"Weekend days: {weekend}")

    # Example of using Switch
    switch = Switch.ON
    print(f"Switch is: {switch.name}")


if __name__ == "__main__":
    main()
