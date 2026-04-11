"""
Arbitrary Arguments and Keyword Arguments.
"""
# *args     = allows you to pass
#             multiple non-key arguments (as a tuple).
# *kwargs   = allows you to pass
#             multiple keyword-arguments (as a dictionary).
#             * unpacking operator.
#             1. positional,
#             2. default,
#             3. keyword,
#             4. ARBITRARY.


def add_0(a, b) -> int:
    """ Function that adds two numbers.
    """
    print(f"Adding {a} and {b}...")
    return a + b


def add_1(*args) -> int:
    """ Function that adds multiple numbers.
    """
    total = 0
    for arg in args:
        total += arg
    return total


def add_1_1(*nums) -> int:
    """ Function that adds multiple numbers.
    """
    total = 0
    for num in nums:
        total += num
    return total


def add_2(**kwargs) -> int:
    """ Function that adds multiple keyword arguments.
    """
    total = 0
    for value in kwargs.values():
        total += value
    return total


def display_name(*args) -> None:
    """ Function that displays a name.
    """
    for arg in args:
        print(arg, end=" ")


def print_address(**kwargs) -> None:
    """ Function that prints an address.
    """
    print(type(kwargs))


def print_address_1(**kwargs) -> None:
    """ Function that prints an address.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def shipping_info(*args, **kwargs) -> None:
    """ Function that prints shipping information.
    """
    print("Shipping Information:")
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


def shipping_info_1(*args, **kwargs) -> None:
    """ Function that prints shipping information.
    """
    print("Shipping Information:")
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(kwargs.get('street'))
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")


class Schema():
    """ Schema class.
    """
    def __init__(self, **kwargs) -> None:
        """ Constructor.
        """
        self.schema = kwargs

    def display_schema(self) -> None:
        """ Method to display the schema.
        """
        for key, value in self.schema.items():
            print(f"{key}: {value}")

    def update_schema(self, **kwargs) -> None:
        """ Method to update the schema.
        """
        self.schema.update(kwargs)

    def get_schema(self) -> dict:
        """ Method to get the schema.
        """
        return self.schema

    def delete_schema(self) -> None:
        """ Method to delete the schema.
        """
        self.schema.clear()

    def __str__(self) -> str:
        """ String representation of the schema.
        """
        return str(self.schema)

    def __repr__(self) -> str:
        """ Official string representation of the schema.
        """
        return f"Schema({self.schema})"

    def __len__(self) -> int:
        """ Method to get the length of the schema.
        """
        return len(self.schema)

    def __contains__(self, key) -> bool:
        """ Method to check if a key is in the schema.
        """
        return key in self.schema

    def __getitem__(self, key):
        """ Method to get a value from the schema.
        """
        return self.schema[key]

    def __setitem__(self, key, value) -> None:
        """ Method to set a value in the schema.
        """
        self.schema[key] = value

    def __delitem__(self, key) -> None:
        """ Method to delete a key from the schema.
        """
        del self.schema[key]


def main() -> None:
    """ Main function.
    """
    # Demonstrating the use of *args and **kwargs:
    # add_0(1, 2)  # Output: 3
    print(add_0(1, 2))
    # add_1(1, 2, 3, 4, 5)  # Output: 15
    print(add_1(1, 2, 3, 4, 5))
    # add_1_1(1, 2, 3, 4, 5)  # Output: 15
    print(add_1_1(1, 2, 3, 4, 5))
    # add_2(a=1, b=2, c=3, d=4, e=5)  # Output: 15
    print(add_2(a=1, b=2, c=3, d=4, e=5))
    # display_name("John", "Doe")  # Output: John Doe
    display_name("John", "Doe")
    print()  # New line for better readability.
    # print_address(street="123 Main St",
    # city="Anytown", state="CA", zip="12345")
    print_address(street="123 Main St",
                  city="Anytown",
                  state="CA",
                  zip="12345")
    # print_address_1(street="123 Main St",
    # city="Anytown", state="CA", zip="12345")
    print_address_1(street="123 Main St",
                    city="Anytown",
                    state="CA",
                    zip="12345")
    # shipping_info("John Doe",
    #               street="123 Main St",
    #               city="Anytown",
    #               state="CA",
    #               zip="12345")
    shipping_info("John Doe",
                  street="123 Main St",
                  city="Anytown",
                  state="CA",
                  zip="12345")
    # shipping_info_1("John Doe",
    #               street="123 Main St",
    #               apt="Apt 4B",
    #               city="Anytown",
    #               state="CA",
    #               zip="12345")
    shipping_info_1("John Doe",
                    street="123 Main St",
                    apt="Apt 4B",
                    city="Anytown",
                    state="CA",
                    zip="12345")
    shipping_info_1("John Doe",
                    street="123 Main St",
                    pobox="P.O. Box 5678",
                    city="Anytown",
                    state="CA",
                    zip="12345")

    # Demonstrating the use of the Schema class:
    class Person(Schema):
        """ PersonSchema class that inherits from Schema.
        """
        def __init__(self, name, age, **kwargs) -> None:
            """ Constructor.
            """
            self.name = name
            self.age = age
            super().__init__(**kwargs)

    person = Person(name="John Doe", age=30)
    print(f"{person}")  # Output: {'name': 'John Doe', 'age': 30}


if __name__ == "__main__":
    main()
