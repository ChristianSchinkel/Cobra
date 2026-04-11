""" Decorators.
"""
# Decorator = A function that extends the behavior
#             of another function without modifying
#             the base function. Pass the base function
#             as an argument to the decorator:


def add_sprinkles(func):
    """ Decorator that adds sprinkles to a cake.
    """
    def wrapper(*args, **kwargs):
        """ Wrapper function that adds sprinkles to the cake.
        """
        print("Adding sprinkles...")
        func(*args, **kwargs)
    return wrapper


def add_chocolate(func):
    """ Decorator that adds chocolate to a cake.
    """
    def wrapper(*args, **kwargs):
        """ Wrapper function that adds chocolate to the cake.
        """
        print("Adding chocolate...")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_chocolate
def make_cake(flavor) -> None:
    """ Function that makes a cake.
    """
    print(f"Making a {flavor} cake...")


def main():
    """ Main function.
    """
    make_cake("chocolate")


if __name__ == "__main__":
    main()
