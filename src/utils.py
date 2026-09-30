"""
Utility functions for the workshop demo.
"""

from datetime import date

Number = int | float


def greet(name: str) -> str:
    """Greet a person with a welcome message.

    Args:
        name: Person's name.

    Returns:
        Greeting message.

    Raises:
        TypeError: If name is not a string.
        ValueError: If name is empty.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a non-empty string")
    if not name:
        raise ValueError("Name must be a non-empty string")
    return f"Hello, {name}! Welcome to the Git workshop!"


def calculate_age(birth_year: int) -> int:
    """Calculate age based on birth year.

    Args:
        birth_year: Year of birth.

    Returns:
        Current age.

    Raises:
        TypeError: If birth_year is not an integer.
        ValueError: If birth_year is in the future.
    """
    if isinstance(birth_year, bool) or not isinstance(birth_year, int):
        raise TypeError("Birth year must be a number")
    if birth_year <= 0:
        raise ValueError("Birth year must be a positive number")

    current_year = date.today().year
    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future")

    return current_year - birth_year


def format_date(value: date) -> str:
    """Format a date to a readable string, e.g. 'January 15, 2024'.

    Args:
        value: Date to format.

    Returns:
        Formatted date string.

    Raises:
        TypeError: If value is not a date.
    """
    if not isinstance(value, date):
        raise TypeError("Input must be a date object")

    return f"{value.strftime('%B')} {value.day}, {value.year}"


def add(a: Number, b: Number) -> Number:
    """Add two numbers (students can extend this).

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract two numbers (students can extend this).

    Args:
        a: First number.
        b: Second number.

    Returns:
        Difference of a and b.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of a and b.

    Raises:
        TypeError: If either argument is not a number.
    """
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, int | float):
            raise TypeError("Both arguments must be numbers")
    return a * b
