"""Address module."""


class Address:
    """Represents an address."""
    def __init__(self, street: str, zip_code: str, city: str, country: str):
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the Address instance.

        The string is formatted as:
        "Address(<street>, <zip_code>, <city>, <country>)"
        using the instance's attributes. This representation is intended for
        debugging and logging and returns a str.
        """
        return (f"Address({self.street}, {self.zip_code}, "
                f"{self.city}, {self.country})"
                )

    def __str__(self) -> str:
        """
        Return a readable string representation of the Address instance.

        The string is formatted as:
        "<street>, <zip_code> <city>, <country>" using the instance's
        attributes. This representation is intended for end-users and returns
        a str.
        """
        return (f"{self.street}, {self.zip_code} "
                f"{self.city}, {self.country}"
                )


def main():
    """Main function for testing the Address class."""
    addr = Address("123 Main St", "12345", "Anytown", "Anycountry")
    print(
        f"Address: {addr.street}, {addr.zip_code} {addr.city}, {addr.country}"
        )


if __name__ == "__main__":
    main()
