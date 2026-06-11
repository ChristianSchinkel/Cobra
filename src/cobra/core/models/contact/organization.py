"""Organization module."""


class Organization:
    """Represents an organization."""
    def __init__(self, name: str):
        self.name = name
        self.address = None
        self.email = None
        self.phone_number = None

    def set_address(self, address):
        """Sets the address of the organization."""
        self.address = address

    def set_email(self, email):
        """Sets the e-mail address of the organization."""
        self.email = email

    def set_phone_number(self, phone_number):
        """Sets the phone number of the organization."""
        self.phone_number = phone_number

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the Organization
        instance.

        The string is formatted as "Organization(<name>)" using the
        instance's name attribute. This representation is intended for
        debugging and logging and returns a str.
        """
        return f"Organization({self.name})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the Organization instance.

        The string is formatted as "<name>" using the instance's name
        attribute. This representation is intended for end-users and returns
        a str.
        """
        return (f"{{\n Name: {self.name},\n"
                f" Address: {self.address},\n"
                f" Email: {self.email},\n"
                f" Phone Number: {self.phone_number}" + "\n}"
                )


def main() -> None:
    """Main function for testing the Organization class."""
    org = Organization("Example Org")
    org.set_phone_number("+123456789")
    print(f"Organization: {org.name}, Phone: {org.phone_number}")


if __name__ == "__main__":
    main()
