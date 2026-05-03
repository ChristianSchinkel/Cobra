"""CLI strings for any application."""
# import argparse
import time


def print_divider(title: str = "", length: int = 50, char: str = "-") -> None:
    """Generate a divider string with an optional title."""
    if title:
        title = f" {title} "
        padding_length = (length - len(title)) // 2
        print(char * padding_length + title + char * padding_length)

    print(char * length)


def print_bordered_message(message: str, border_char: str = "*") -> None:
    """Print a message with a border around it."""
    border_length = len(message) + 4
    print(border_char * border_length)
    print(f"{border_char} {message} {border_char}")
    print(border_char * border_length)


def print_bordered_multiline_message(messages: list[str],
                                     border_char: str = "*") -> None:
    """Print multiple messages with a border around them."""
    max_length = max(len(msg) for msg in messages) + 4
    print(border_char * max_length)
    for msg in messages:
        print(f"{border_char} {msg.ljust(max_length - 4)} {border_char}")
    print(border_char * max_length)


def print_menu(options: list[str], title: str = "Menu") -> None:
    """Print a numbered menu of options."""
    print_divider(title)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print_divider()


def present_loading_bar_cli(total: int,
                            prefix: str = "Loading",
                            suffix: str = "Complete",
                            length: int = 50) -> None:
    """Present a loading bar in the CLI."""
    for i in range(total + 1):
        percent = (i / total) * 100
        filled_length = int(length * i // total)
        bar_tile = "█" * filled_length + "-" * (length - filled_length)
        print(f"\r{prefix} |{bar_tile}| {percent:.2f}% {suffix}", end="")
        time.sleep(0.1)
    print()
