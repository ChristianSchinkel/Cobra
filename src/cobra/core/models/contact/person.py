"""Person module."""


class Person:
    """Represents a person.
    first_name: str - The first name of the person.
    last_name: str - The last name of the person.
    Optional:
    person_number: PersonNumber - The person's identification number.
    """
    def __init__(self, first_name: str, last_name: str, person_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.person_number = person_number
        self.address = None
        self.email = None
        self.phone_number = None

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the Person instance.

        The string is formatted as "Person(<first_name> <last_name>)" using the
        instance's self.first_name and self.last_name attributes. This
        representation is intended for debugging and logging and returns a str.
        """
        return f"Person({self.first_name} {self.last_name})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the Person instance.

        The string is formatted as "<first_name> <last_name>" using the
        instance's self.first_name and self.last_name attributes. This
        representation is intended for end-users and returns a str.
        """
        return ("{\n" + f" Name: {self.first_name}, {self.last_name},\n"
                f" Person Number: {self.person_number},\n"
                f" Address: {self.address},\n"
                f" Email: {self.email},\n"
                f" Phone Number: {self.phone_number}" + "\n}"
                )

    def set_address(self, address):
        """Sets the address of the person."""
        self.address = address

    def set_email(self, email):
        """Sets the e-mail address of the person."""
        self.email = email

    def set_phone_number(self, phone_number):
        """Sets the phone number of the person."""
        self.phone_number = phone_number


def main() -> None:
    """Main function for testing the Person class."""
    person = Person("John", "Doe")
    person.set_phone_number("+123456789")
    print(person)


if __name__ == "__main__":
    main()
