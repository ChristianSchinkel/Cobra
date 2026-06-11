"""Bank Organization Module."""

from ..contact.organization import Organization


class Bank(Organization):
    """Represents a bank organization."""

    def __init__(self, name: str):
        super().__init__(name)
        self.swift_code: str = ""

    def set_swift_code(self, swift_code: str):
        """Sets the SWIFT code of the bank."""
        self.swift_code = swift_code


def main() -> None:
    """Main function for testing the Bank class."""
    bank = Bank("Example Bank")
    bank.swift_code = "EXAMPBANK"
    print(f"Bank: {bank.name}, "
          f"SWIFT Code: {bank.swift_code}"
          )


if __name__ == "__main__":
    main()
