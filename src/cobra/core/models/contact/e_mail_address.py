"""E-mail address module."""


class EmailAddress:
    """Represents an e-mail address.
    Attributes:
        email (str): The e-mail address.
    """
    def __init__(self, email: str):
        self.email = email

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the EmailAddress
        instance.

        The string is formatted as "EmailAddress(<email>)" using the
        instance's email attribute. This representation is intended for
        debugging and logging and returns a str.
        """
        return f"EmailAddress({self.email})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the EmailAddress instance.

        The string is formatted as "<email>" using the instance's email
        attribute. This representation is intended for end-users and returns
        a str.
        """
        return self.email


def main():
    """Main function for testing the EmailAddress class."""
    email = EmailAddress("example@example.com")
    print(f"E-mail Address: {email.email}")


if __name__ == "__main__":
    main()
