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


if __name__ == "__main__":
    main()
