#!/usr/bin/env python
"""
The Cobra application.
"""

from src.utils.cli_ui import CLui, InputController


def app(running=True) -> None:
    """Main function to run the Cobra application."""
    # Initialize the CLI UI and Input Controller
    ui = CLui()
    ic = InputController()

    while running is True:
        # Clear the screen and display the main menu
        pass

    # Loading bar demonstration
    ui.display_loading_bar_cli(total=100, length=30)
    # Display a welcome message
    ui.display_bordered_message("Welcome to Cobra!", border_char="#")
    # Display the main menu
    ui.display_menu("About", "Settings", "Load Data", "Help", "Exit", title="Main Menu")
    # Get user input for menu selection
    selection = ic.format_int("Please select an option (1-5): ")
    # Handle user selection (this is just a placeholder for actual functionality)
    about = "Cobra is a powerful CLI application for data processing."
    settings = "Settings are currently unavailable."
    load_data = "Data loading is currently unavailable."
    help_msg = "Help is currently unavailable."
    exit_msg = "Exiting Cobra. Goodbye!"
    default = "Invalid selection. Please try again." + "\n" + exit_msg

    if selection == 1:
        ui.display_bordered_message(about, border_char="#")
    elif selection == 2:
        ui.display_bordered_message(settings, border_char="#")
    elif selection == 3:
        ui.display_bordered_message(load_data, border_char="#")
    elif selection == 4:
        ui.display_bordered_message(help_msg, border_char="#")
    elif selection == 5:
        ui.display_bordered_message(exit_msg, border_char="#")
    else:
        ui.display_bordered_message(default, border_char="#")


def main() -> None:
    """Main function to run the application."""
    app()


if __name__ == "__main__":
    main()
