"""CLI UIs for any application."""
# import argparse
from dataclasses import dataclass
import time

PROGRAM_INDENT = ">>> "


@dataclass
class CLui:
    """A class for CLI utilities."""
    program_name: str = "My CLI Application"
    version: str = "1.0.0"
    description: str = "A simple CLI application."

    @staticmethod
    def welcome_message() -> None:
        """Print a welcome message with program details."""
        p = PROGRAM_INDENT
        print(f"{p}Welcome to {CLui.program_name}"
              f"{p}(version {CLui.version})!")
        print(f"{p}{CLui.description}")
        print(f"{p}Type 'help' for a list of commands.")

    @staticmethod
    def end_session() -> None:
        """Print a message indicating the end of a session."""
        print(f"{PROGRAM_INDENT}Session ended. Goodbye!")

    @staticmethod
    def table(*args: str, column_width: int = 20) -> None:
        """Format a row of data into columns with specified width."""
        # Print a header row line for the table
        if args:
            print("-" * (len(args) * (column_width + 3) - 3))
        # Format each argument to be left-aligned within the specified column width
        print(" | ".join(arg.ljust(column_width) for arg in args))
        print("-" * (len(args) * (column_width + 3) - 3))

    @staticmethod
    def padded_label(label: str, width: int = 20) -> str:
        """Return a label padded to a specific width."""
        return label.center(width)

    @staticmethod
    def display_divider(title: str = "", length: int = 50, symbol: str = "-") -> None:
        """Generate a divider string with an optional title."""
        if title:
            title = f" {title} "
            padding_length = (length - len(title)) // 2
            print(symbol * padding_length + title + symbol * padding_length)

        print(symbol * length)

    @staticmethod
    def display_bordered_message(msg: str, border_char: str = "*") -> None:
        """Print a message with a border around it."""
        border_length = len(msg) + 4
        print(border_char * border_length)
        print(f"{border_char} {msg} {border_char}")
        print(border_char * border_length)

    @staticmethod
    def display_bordered_multiline_message(*args: str, border_char: str = "*") -> None:
        """Print multiple messages with a border around them."""
        max_length = max(len(msg) for msg in args) + 4
        print(border_char * max_length)
        for msg in args:
            print(f"{border_char} {msg.ljust(max_length - 4)} {border_char}")
        print(border_char * max_length)

    @staticmethod
    def display_menu(*args: str, title: str = "Menu") -> None:
        """Print a numbered menu of options."""
        CLui.display_divider(title)
        for i, option in enumerate(args, start=1):
            print(f"{i}. {option}")
        CLui.display_divider()

    @staticmethod
    def display_loading_bar_cli(total: int,
                                length: int = 50) -> None:
        """Present a loading bar in the CLI."""
        prefix: str = "Loading"
        suffix: str = "Complete"

        for i in range(total + 1):
            percent = (i / total) * 100
            filled_length = int(length * i // total)
            bar_tile = "█" * filled_length + "-" * (length - filled_length)
            print(f"\r{prefix} |{bar_tile}| {percent:.2f}% {suffix}", end="")
            time.sleep(0.1)
        print()


class InputController:
    """Class to handle input control."""
    p = PROGRAM_INDENT

    def __init__(self):
        """Initialize the Input Controller."""

    def check_input_is_string(self, user_input: str) -> bool:
        """Check if the input is a string."""
        return isinstance(user_input, str)

    def format_int(self, prompt: str) -> int:
        """Format the input as an integer. If it fails,
        raises a ValueError. And ask the user to input again.
        :param prompt: The prompt to display to the user.
        :return: The formatted integer.
        """
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print(self.p + "Invalid input. Please enter an integer.")

    def format_float(self, prompt: str) -> float:
        """Format the input as a float. If it fails,
        raises a ValueError. And ask the user to input again.
        :param prompt: The prompt to display to the user.
        :return: The formatted float.
        """
        while True:
            try:
                # Check for ', or '.' in input but not both
                user_input = input(prompt)
                removed_thousands = (
                    self.thousand_separator_remover(user_input)
                )
                normalized_decimal = (
                    self.decimal_normalizer(removed_thousands)
                )
                if self.is_integer(normalized_decimal):
                    print(
                        self.p
                        + "Input appears to be an integer. Please enter a float."
                    )
                    continue
                return float(normalized_decimal)
            except ValueError:
                print("Invalid input. Please enter a float.")

    def format_bool(self, prompt: str) -> bool:
        """Format the input as a boolean. If it fails,
        raises a ValueError. And ask the user to input again.
        :param prompt: The prompt to display to the user.
        :return: The formatted boolean.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'y', 'true', 't']:
                return True
            elif response in ['no', 'n', 'false', 'f']:
                return False
            else:
                print("Invalid input. Please enter yes or no.")

    def contain_float_separator(self, user_input: str) -> bool:
        """Check if the input has a '.' or a ',' to determine if it's a float."""
        return '.' in user_input or ',' in user_input

    def is_integer(self, user_input: str) -> bool:
        """Check if the input string contains a float separator.
        and if it does, return False.
        If the input contains string characters
        other than numbers, return False.
        """
        # If the input has a float separator, it's not an integer.
        has_float_separator = self.contain_float_separator(user_input)
        # If the input contains only digits, it's an integer.
        is_digit = user_input.isdigit()

        # Return True only if it's all digits and has no float separator.
        return is_digit and not has_float_separator

    def replace_float_separator(self, user_input: str) -> str:
        """Replace ',' with '.' in the input string."""
        return user_input.replace(',', '.')

    def is_floatable(self, user_input: str) -> bool:
        """Check if the input string can be converted to a float.

        The string must contain numbers and a float seperoator.
        then return True.

        If the input contains string characters
        other than numbers and a float separator,
        return False.
        """
        has_float_separator = self.contain_float_separator(user_input)
        # Remove float separators for digit check
        cleaned_input = user_input.replace('.', '').replace(',', '')
        is_digit = cleaned_input.isdigit()

        return has_float_separator and is_digit

    def thousand_separator_remover(self, user_input: str) -> str:
        """Remove thousand separators from the input string:
        If the input has both '.' and ',', assume one is a thousand separator."""
        if '.' in user_input and ',' in user_input:
            if user_input.index('.') < user_input.index(','):
                # Assume '.' is thousand separator
                return user_input.replace('.', '')
            else:
                # Assume ',' is thousand separator
                return user_input.replace(',', '')
        return user_input

    def decimal_normalizer(self, user_input: str) -> str:
        """Normalize the decimal separator to '.'."""
        if ',' in user_input:
            return user_input.replace(',', '.')
        return user_input
