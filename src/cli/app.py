import os
import shutil
import time

from src.automata import ElementaryAutomata
from .messages import SECTIONS


def clear_display():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def center_text(text: str) -> str:
    """
    Center the text horizontally in the terminal.
    :param text: Text to center
    :return: The centered text
    """
    terminal_width = shutil.get_terminal_size().columns
    centered_text = '\n'.join(line.center(terminal_width) for line in text.split('\n'))
    return centered_text


def display_section(section: str):
    """
    Displays a section centered.

    :param section: The section to display
    """
    centered_text = center_text(section)
    print(centered_text)


def continue_with_enter(message: str):
    """
    Displays a message and waits the user to press enter to continue.

    :param message: Message to print
    """
    print(message, end='', flush=True)
    input()
    print('\033[1A\033[K', end='', flush=True)


def display_info():
    """Displays the sections."""
    clear_display()

    for section in SECTIONS:
        display_section(f'\n\n{section}')
        continue_with_enter('Press enter to continue...')

    continue_with_enter('\n\n\033[93mDo you want to proceed to the simulation? This will clear the screen.'
                        '\nPress enter to start the simulation...\033[0m')

    clear_display()


def validate_input(prompt: str, validation_fn, error_message: str) -> str:
    """
    Validates user input.

    :param prompt: Prompt to display.
    :param validation_fn: Callback function to validate the input.
    :param error_message: Error message to display
    :return: The validated input
    """
    while True:
        user_input = input(prompt)
        print('\033[1A\033[K', end='', flush=True)
        if validation_fn(user_input):
            clear_display()
            return user_input
        else:
            print(f"\033[91mInvalid Input \"{user_input}\". {error_message}\033[0m")


def get_user_input() -> tuple:
    """Collect and validate user inputs."""
    size = validate_input(
        "Enter the size of the automaton (positive integer): ",
        lambda x: x.isdigit() and int(x) > 0,
        "Please enter a positive integer."
    )
    rule = validate_input(
        "Enter the rule number (0-255): ",
        lambda x: x.isdigit() and 0 <= int(x) <= 255,
        "Please enter a number between 0 and 255."
    )
    boundary_conditions = ['fixed_dead', 'fixed_alive', 'periodic', 'adiabatic', 'reflexive']
    boundary_condition = validate_input(
        f"Enter the boundary condition {boundary_conditions}: ",
        lambda x: x.strip().lower() in boundary_conditions,
        f"Please enter one of the following: {', '.join(boundary_conditions)}."
    ).strip().lower()
    generations = validate_input(
        "Enter the number of generations to simulate: ",
        lambda x: x.isdigit() and int(x) > 0,
        "Please enter a positive integer."
    )
    return int(size), int(rule), boundary_condition, int(generations)


def app():
    """Main function to run the console application."""
    display_info()

    size, rule, boundary_condition, generations = get_user_input()

    print("The simulation will run with the following settings:")
    print(f"  - Size: {size}")
    print(f"  - Rule: {rule}")
    print(f"  - Boundary Condition: {boundary_condition}")
    print(f"  - Generations: {generations}")
    input("\n\033[93mPress Enter to start the simulation...\033[0m")

    clear_display()

    automata = ElementaryAutomata(size=size, rule=rule, boundary_condition=boundary_condition)

    for _ in range(generations):
        print(center_text(str(automata)))
        automata.evolve()
        time.sleep(0.1)

    print('\n\n\n')

