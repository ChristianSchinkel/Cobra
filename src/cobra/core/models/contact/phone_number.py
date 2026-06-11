"""Phone number module."""


class PhoneNumber:
    """Represents a phone number."""
    def __init__(self, number: str):
        self.number = number

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the PhoneNumber
        instance.

        The string is formatted as "PhoneNumber(<number>)" using the
        instance's number attribute. This representation is intended for
        debugging and logging and returns a str.
        """
        return f"PhoneNumber({self.number})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the PhoneNumber instance.

        The string is formatted as "<number>" using the instance's number
        attribute. This representation is intended for end-users and returns
        a str.
        """
        return self.number


def main() -> None:
    """Main function for testing the PhoneNumber class."""
    phone = PhoneNumber("+123456789")
    print(f"Phone Number: {phone.number}")


if __name__ == "__main__":
    main()
