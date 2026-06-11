""" Decorators.
"""
# Decorator = A function that extends the behavior
#             of another function without modifying
#             the base function. Pass the base function
#             as an argument to the decorator:

from functools import wraps
from typing import Callable, Any
import time


def get_time(func: Callable) -> Callable:
    """ Decorator that measures the execution time of a function.
    """
    # Preserve the original function's metadata …
    @wraps(func)  # …(name, docstring, etc.)
    def wrapper(*args, **kwargs) -> Any:
        """ Wrapper function that measures the execution time
        of the original function.
        Args:
            *args: Positional arguments for the original function.
            **kwargs: Keyword arguments for the original function.
        Returns:
            Any: The result of the original function.
        """
        start_time: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = time.perf_counter()
        print(f"Ran {func.__name__} in {end_time - start_time:.2f} seconds")

        return result

    return wrapper


@get_time
def expensive_function() -> None:
    """
    A function that simulates an expensive operation.
    Returns:
        None
    """
    time.sleep(2)  # Simulate an expensive operation
    print("Done!")


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

    # Measure the execution time of the expensive function
    print(expensive_function.__name__)
    print(expensive_function.__doc__)
    print(expensive_function.__annotations__)
    expensive_function()


if __name__ == "__main__":
    main()
