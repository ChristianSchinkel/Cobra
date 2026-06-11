"""Person number module."""

from __future__ import annotations
from InputController import InputController


class PersonNumber:
    """Represents a person number."""
    def __init__(self, year: int, month: int, day: int, serial: str):
        self.year = year
        self.month = month
        self.day = day
        self.serial = serial

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the PersonNumber
        instance.

        The string is formatted as:
        "PersonNumber(<year>-<month>-<day>-<serial>)"
        using the instance's attributes. This representation is intended for
        debugging and logging and returns a str.
        """
        return (f"PersonNumber({self.year}-{self.month:02d}-"
                f"{self.day:02d}-{self.serial})"
                )

    def __str__(self) -> str:
        """
        Return a readable string representation of the PersonNumber instance.

        The string is formatted as "<year>-<month>-<day>-<serial>" using the
        instance's attributes. This representation is intended for end-users
        and returns a str.
        """
        return f"{self.year}-{self.month:02d}-{self.day:02d}-{self.serial}"

    @staticmethod
    def create_instance() -> PersonNumber:
        """Create a PersonNumber instance."""
        ic = InputController()
        year = ic.format_int(prompt="Enter birth year (YYYY): ")
        month = ic.format_int(prompt="Enter birth month (MM): ")
        day = ic.format_int(prompt="Enter birth day (DD): ")
        serial = input("Enter person serial number: ")
        return PersonNumber(year, month, day, serial)


def main() -> None:
    """Main function for testing the PersonNumber class."""
    pn = PersonNumber.create_instance()
    print(f"Person Number: {pn.year}-{pn.month:02d}-{pn.day:02d}-{pn.serial}")


if __name__ == "__main__":
    main()
