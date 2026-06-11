"""Bank Account Module."""
from .bank import Bank


class BankAccount:
    """Represents a bank account."""

    def __init__(self, account_number: str, bank: Bank, balance: float = 0.0):
        self.account_number = account_number
        self.bank = bank
        self.balance = balance

    def __repr__(self) -> str:
        """
        Return an unambiguous string representation of the BankAccount
        instance.

        The string is formatted as "BankAccount(<account_number>)" using the
        instance's account_number attribute. This representation is intended
        for debugging and logging and returns a str.
        """
        return f"BankAccount({self.account_number})"

    def __str__(self) -> str:
        """
        Return a readable string representation of the BankAccount instance.

        The string is formatted as:
        "Account Number: <account_number>, Bank: <bank_name>,
        Balance: <balance>" using the instance's attributes.
        This representation is intended for end-users and returns a str.
        """
        return (f"{{\n Account Number: {self.account_number},\n"
                f" Bank: {self.bank.name},\n"
                f" Balance: {self.balance}" + "\n}"
                )


def main() -> None:
    """Main function for testing the BankAccount class."""
    bank = Bank("Example Bank")
    account = BankAccount("987654321", bank, 1000.0)
    print(f"Bank Account: {account.account_number}, "
          f"Bank: {account.bank.name}, "
          f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
