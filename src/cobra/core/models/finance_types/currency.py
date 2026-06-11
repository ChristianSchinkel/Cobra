"""Currency Module."""


class Currency:
    """Represents a currency."""

    def __init__(self, code: str, name: str, symbol: str):
        self.code = code
        self.name = name
        self.symbol = symbol

    def __repr__(self) -> str:
        return (
            f"Currency(code='{self.code}', "
            f"name='{self.name}', "
            f"symbol='{self.symbol}')"
        )

    def __str__(self) -> str:
        return f"{self.name} ({self.code}) - {self.symbol}"


def main() -> None:
    """Main function for testing the Currency class."""
    currency = Currency("USD", "United States Dollar", "$")
    print(currency)
    print(repr(currency))


if __name__ == "__main__":
    main()
