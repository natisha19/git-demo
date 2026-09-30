"""Demo entry point for the Git, GitHub & GitHub Actions workshop."""

from datetime import date

import pyfiglet
from colorama import Fore, init

from src.utils import add, calculate_age, format_date, greet, subtract, multiply

# multiply

init(autoreset=True)


def main() -> None:
    """Print the banner and demo the utility functions."""
    print("-", greet("Students"))
    
    print("- Adding 5 and 3 gives", add(5, 3))
    print("- Subtracting 4 from 10 gives", subtract(10, 4))
    print("- Multiplying 6 and 7 gives", multiply(6, 7))  # Uncomment once implemented

    print(Fore.MAGENTA + "\n Ready to start learning Git and GitHub Actions!")


if __name__ == "__main__":
    main()
