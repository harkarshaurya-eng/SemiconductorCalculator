"""Helper functions for input, formatting, and simple user interaction."""


def print_header():
    """Print the main project heading."""
    print("========================================")
    print(" SEMICONDUCTOR FORMULA CALCULATOR")
    print("========================================")


def print_formula(title, formula_lines):
    """Display a formula section before asking for inputs."""
    print(f"\n{title}")
    print("-" * len(title))
    for line in formula_lines:
        print(line)


def safe_float_input(prompt, allow_zero=True, allow_negative=False):
    """Read a float safely and keep asking until the value is valid."""
    while True:
        user_input = input(prompt).strip()

        try:
            value = float(user_input)
        except ValueError:
            # This prevents the program from crashing on text input.
            print("Invalid input. Please enter a numeric value.")
            continue

        if not allow_negative and value < 0:
            print("Negative values are not allowed here.")
            continue

        if not allow_zero and value == 0:
            print("Zero is not allowed here.")
            continue

        return value


def safe_int_input(prompt, minimum=None, maximum=None):
    """Read an integer safely and keep asking until the value is in range."""
    while True:
        user_input = input(prompt).strip()

        try:
            value = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a value greater than or equal to {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Please enter a value less than or equal to {maximum}.")
            continue

        return value


def ask_continue():
    """Ask whether the user wants to return to the menu for another calculation."""
    while True:
        choice = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()

        if choice == "y":
            return True
        if choice == "n":
            return False

        print("Please enter 'y' for yes or 'n' for no.")


def format_number(value):
    """Format large and small values in a beginner-friendly way."""
    if value == 0:
        return "0"

    if abs(value) >= 10000 or abs(value) < 0.001:
        return f"{value:.6e}"

    return f"{value:.6f}".rstrip("0").rstrip(".")


def show_result(label, value, unit):
    """Print a final answer with units."""
    print(f"\n{label} = {format_number(value)} {unit}")
