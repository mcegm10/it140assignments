"""Calculates a user's approximate birth year.

Input:
    user_name: string from keyboard input
    user_age: integer from keyboard input

Process:
    user_born = CURRENT_YEAR - user_age

Output:
    Greeting and approximate birth year

Typical usage example:
    Enter your name: Megan
    Enter your age: 44
    Hello Megan! You were born in 1982.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_born = CURRENT_YEAR - user_age
    print(f"Hello {user_name}! You were born in {user_born}.")


# === Main Guard ===
if __name__ == "__main__":
    main()
